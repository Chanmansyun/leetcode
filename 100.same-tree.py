#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if not p and not q:
        #     return True
        # elif not (p and q):
        #     return False
        # elif p.val != q.val:
        #     return False
        # elif (p.left is None and q.left) or (q.left and p.left is None):
        #     return False
        # elif (p.right is None and q.right) or (q.right and p.right is None):
        #     return False
        
        # if not p.left and not p.right and not q.left and not q.right:
        #     return True
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return p == q

# @lc code=end

