#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.minDepth(root.left) 
        right = self.minDepth(root.right)
        
        if left != 0 and right != 0:
            return min(left, right) + 1
        else:
            return left + 1 if left !=0 else right + 1
# @lc code=end

