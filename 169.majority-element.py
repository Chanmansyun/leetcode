#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = nums[0]
        cnt = 1
        for i in nums[1:]:
            if  maj == i:
                cnt += 1
            elif maj != i:
                cnt -= 1
            if cnt == 0:
                maj = i
                cnt = 1
        return maj
# @lc code=end

