#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # if m == 0:
        #     nums1[:n] = nums2
        
        # if m !=0 and n != 0:
        #     for i in range(m):
        #         if nums1[i] > nums2[0]:
        #             nums1[i], nums2[0] = nums2[0], nums1[i]
        #         for z in range(n-1):
        #             if nums2[z] > nums2[z+1]:
        #                 nums2[z], nums2[z+1] = nums2[z+1], nums2[z]
        #             elif nums2[z] <= nums2[z+1]:
        #                 break
        # nums1[m:] = nums2
        
        mn = m + n - 1
        while n > 0:
            if m > 0 and nums1[m-1] >= nums2[n-1]:
                nums1[mn] = nums1[m-1]
                m -= 1
            else:
                nums1[mn] = nums2[n-1]
                n -= 1
            mn -= 1
                
# @lc code=end

