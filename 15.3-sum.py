#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            target = nums[i]
            if result and target==result[-1][0]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                if target+nums[l]+nums[r] < 0:
                    l += 1
                elif target+nums[l]+nums[r] > 0:
                    r -= 1
                elif target+nums[l]+nums[r] == 0:
                    result.append([target, nums[l], nums[r]])
                    while l<r and nums[l]==result[-1][1]: l += 1
                    while l<r and nums[r]==result[-1][-1]: r -= 1
        return result
        
# @lc code=end

