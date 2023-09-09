#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     if nums[0] >= target:
    #         return 0
    #     elif nums[-1] < target:
    #         return len(nums)
    #     elif nums[-1] == target:
    #         return len(nums)-1
        
    #     length = len(nums)
    #     mid = length//2
    #     if nums[mid] > target:
    #         if nums[mid-1] < target:
    #             return mid
    #         sub_idx = self.searchInsert(nums[:mid], target)
    #         mid = 0
    #     elif nums[mid] < target:
    #         if nums[mid+1] >= target:
    #             return mid+1
    #         sub_idx = self.searchInsert(nums[mid:], target)
    #     elif nums[mid] == target:
    #         return mid    
    #     return mid + sub_idx

    # def searchInsert(self, nums: List[int], target: int) -> int:  
    #     if nums[0] >= target:
    #         return 0
    #     elif nums[-1] < target:
    #         return len(nums)
    #     elif nums[-1] == target:
    #         return len(nums)-1      
        
    #     low, high = 0, len(nums)
    #     while True:
    #         mid = (low+high)//2
    #         if nums[mid] > target:
    #             if nums[mid-1] < target:
    #                 return mid
    #             high = mid
    #         elif nums[mid] < target:
    #             if nums[mid+1] > target:
    #                 return mid+1
    #             low = mid
    #         elif nums[mid] == target:
    #             return mid
    
    def searchInsert(self, nums: List[int], target: int) -> int:  
        if not nums:
            return 0
        
        for i, num in enumerate(nums):
            if num >= target:
                return i
        
        return len(nums)
            
# @lc code=end

