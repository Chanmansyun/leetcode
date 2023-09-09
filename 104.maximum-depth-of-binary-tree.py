#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def max_depth(p, q):
            if p and q:
                return 1 + max(max_depth(p.left, p.right), 
                                max_depth(q.left, q.right))
            elif p and not q:
                return 1 + max_depth(p.left, p.right)
            elif not p and q:
                return 1 + max_depth(q.left, q.right)
            elif p == q:
                return 1

        return max_depth(root.left, root.right)
        
        # if not root:
        #     return 0
    
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
# @lc code=end

