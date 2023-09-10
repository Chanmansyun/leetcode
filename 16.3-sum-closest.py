#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0]+nums[1]+nums[2]
        
        for i in range(len(nums)):
            n = nums[i]
            if i>=1 and n==nums[i-1]:
                continue
            l, r = i+1, len(nums)-1

            while l < r:
                temp = n+nums[l]+nums[r]
                if temp < target:
                    if abs(temp-target) < abs(result-target):
                       result = temp
                    l += 1
                elif temp > target:
                    if abs(temp-target) < abs(result-target):
                        result = temp
                    r -= 1
                elif temp == target:
                    return temp
        return result
# @lc code=end

