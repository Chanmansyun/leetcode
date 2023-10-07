#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if target not in nums:
        #     return -1
        # elif len(nums) == 1:
        #     return 0
        
        # l, r = 0, len(nums)-1
        # while l < r:
        #     mid = (l+r)//2
        #     if target == nums[mid]:
        #         return mid
            
        #     if nums[l] < nums[r]:
        #         if nums[mid] < target:
        #             l = mid
        #         elif nums[mid] > target:
        #             r = mid
        #     elif nums[l] > nums[r]:
        #         if nums[mid] > nums[l]:
        #             if target < nums[mid] and target >= nums[l]:
        #                 r = mid
        #             else:
        #                 l = mid
        #         elif nums[mid] < nums[r]:
        #             if target > nums[mid] and target <= nums[r]:
        #                 l = mid
        #             else:
        #                 r = mid

        #     if r-l == 1:
        #         if nums[l] == target:
        #             return l
        #         else:
        #             return r
        
        if len(nums) == 1: 
            if nums[0] == target:
                return 0
            else:
                return -1
            
        l, r = 0, len(nums)-1
        while r-l > 1:
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                l = mid
            elif nums[mid] < nums[l]:
                r = mid
            elif nums[l] < nums[r]:
                break
        
        if nums[l] > nums[r]:
            sp = r
        else:
            sp = l
        
        if target > nums[0]:
            if sp != 0:
                l, r = 0, sp-1
            else:
                l, r = 0, len(nums)-1
        elif target < nums[0]:
            l, r = sp, len(nums)-1
        else:
            return 0

        while r-l > 1:
            mid = (l+r)//2
            if target > nums[mid]:
                l = mid
            elif target < nums[mid]:
                r = mid
            else:
                return mid
                
        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        else:
            return -1
        
                
            

        
        
        
# @lc code=end

