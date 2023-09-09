#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        residual = (columnNumber-1) % 26 + 1
        result = chr(64+residual)
        while columnNumber > 26:
            columnNumber = (columnNumber-residual)//26
            residual = (columnNumber-1) % 26 + 1
            result = chr(64+residual) + result
        return result
# @lc code=end

