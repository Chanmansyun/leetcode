#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:    
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        
        up = self.getRow(rowIndex-1)
        return [1]+[up[j]+up[j+1] for j in range(rowIndex-1)]+[1]
# @lc code=end

