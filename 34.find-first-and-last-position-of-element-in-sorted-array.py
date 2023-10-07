#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        result = [-1, -1]
        l, r = 0, len(nums)-1
        idx = None
        while r-l > 1:
            mid = (l+r)//2
            if target < nums[mid]:
                r = mid
            elif target > nums[mid]:
                l = mid
            else:
                idx = mid
                result = [idx, idx]
                break
        
        if r-l == 1 or r-l == 0:
            if nums[l] == target:
                idx = l
            elif nums[r] == target:
                idx = r
            if idx is not None:
                result = [idx, idx]
            if r-l == 0:
                return result
        
        if idx is not None:
            l, r = max(idx-1, 0), min(len(nums)-1, idx+1)
            while (lp:=nums[l] == target) | (rp:=nums[r] == target):
                if lp and l > 0:
                    l -= 1
                    continue
                if rp and r < len(nums)-1:
                    r += 1
                    continue
                    
                if l == 0 and nums[r] != target:
                    l -= 1
                    break
                elif r == len(nums)-1 and nums[l] != target:
                    r += 1
                    break
                elif l == 0 and r == len(nums)-1:
                    l -= 1
                    r += 1
                    break
                
            result = [l+1, r-1]
        
        return result
# @lc code=end

