#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def maxdepth(p):
            if not p:
                return 0
            else:
                # return max(maxdepth(p.left), maxdepth(p.right)) + 1

        # return abs(maxdepth(root.left)-maxdepth(root.right)) <= 1 \
        #        and self.isBalanced(root.left) and self.isBalanced(root.right)
                left = maxdepth(p.left)
                right = maxdepth(p.right)
                if left == -1 or right == -1:
                    return -1
                if abs(left-right) > 1:
                    return -1
                return max(left, right) + 1
        
        return True if maxdepth(root) != -1 else False
# @lc code=end

