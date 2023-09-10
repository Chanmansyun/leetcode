#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def helper(l, r, string, max):
            result = []
            if l < max:
                result.extend(helper(l+1, r, string+"(", max))
            if l > r:
                result.extend(helper(l, r+1, string+")", max))
            if l == r and l == max:
                return [string]
            return result
        
        return helper(0, 0, "", n)
# @lc code=end

