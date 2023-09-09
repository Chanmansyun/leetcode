#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        unique = 0
        for i in range(len(nums)):
            unique ^= i
        return unique

# @lc code=end

