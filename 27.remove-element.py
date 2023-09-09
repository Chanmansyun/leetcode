#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        
        result = len(nums)
        lt = []
        for j in nums:
            if j == val:
                result -= 1
            else:
                lt.append(j)
        nums[:result-1] = lt
        return result
# @lc code=end

