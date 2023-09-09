#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        pow = len(columnTitle)-1
        for i in columnTitle:
            result += (ord(i)-64) * 26**pow
            pow -= 1
        return result
            
# @lc code=end

