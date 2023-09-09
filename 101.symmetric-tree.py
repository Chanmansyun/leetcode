#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def compare(p, q):
            if p and q:
                return p.val == q.val and compare(p.left, q.right) \
                       and compare(p.right, q.left)
            else:
                return p == q
    
        return compare(root.left, root.right)
        
# @lc code=end

