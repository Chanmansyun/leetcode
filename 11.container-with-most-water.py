#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # [1,2,4,3]
        l_step, r_step = 0, len(height)-1
        result = (r_step-l_step) * min(height[0], height[-1])
        while l_step < r_step:
                result = max(result, (r_step-l_step) * min(height[l_step], height[r_step]))
                if height[l_step] > height[r_step]:
                    r_step -= 1
                elif height[l_step] <= height[r_step]:
                    l_step += 1
        return result
# @lc code=end

