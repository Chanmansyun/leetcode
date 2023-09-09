#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # result = []
        # cont = False
        # for i in range(len(nums)):
        #     if i == len(nums)-1 or nums[i]+1 != nums[i+1]:
        #         if cont:
        #             result.append(f"{start_p}->{nums[i]}")
        #             cont = False
        #         else:
        #             result.append(f"{nums[i]}")
        #     elif nums[i]+1 == nums[i+1]:
        #         if not cont:
        #             cont = True
        #             start_p = nums[i]
        # return result
        
        range = []
        for j in nums:
            if range and range[-1][1]==j-1:
                range[-1][1] = j
            else:
                range.append([j, j])
        return [f"{i[0]}->{i[1]}" if i[0]!=i[1] else f"{i[0]}" for i in range]
            
# @lc code=end

