#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        # elif not root.left and not root.right:
        #     return root.val == targetSum
        # elif root.val > targetSum:
        #     return False
        
        if not root.left and not root.right and targetSum-root.val==0:
            return True
        else:
            return self.hasPathSum(root.left, targetSum-root.val) \
                   or self.hasPathSum(root.right, targetSum-root.val)
        
# @lc code=end

