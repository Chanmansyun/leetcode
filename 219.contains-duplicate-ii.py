#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict = {}
        for i, j in enumerate(nums):
            if not dict.get(j):
                dict[j] = i+1
            elif i+1-dict.get(j) <= k:
                return True
            else:
                dict[j] = i+1
        return False
# @lc code=end

