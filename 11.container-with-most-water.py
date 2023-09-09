#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start_idx = height.index(height.max())
        end_idx = len(height)
        result = (end_idx-start_idx) * min(height[start_idx], height[-1])
        for i, j in enumerate(height):
            if i < start_idx:
                ...
            elif i > start_idx:
                ...
        return result
# @lc code=end

