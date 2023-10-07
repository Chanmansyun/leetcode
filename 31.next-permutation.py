#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if (idx:=len(nums)) != 1:
            idx -= 1
            while idx >= 1 and nums[idx-1] >= nums[idx]:
                idx -= 1
            idx -= 1

            if idx != -1:
                r = nums[idx+1:].index(max(nums[idx+1:]))  + idx + 1
                for i in range(idx+1, len(nums)):
                    if nums[i] > nums[idx] and nums[r] > nums[i]:
                        r = i
                nums[idx], nums[r] = nums[r], nums[idx]
            
            nums[idx+1:] = sorted(nums[idx+1:])
            
# @lc code=end

