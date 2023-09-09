#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # dct = {1: [1], 2: [1,1]}
        # def gen(n, dct):
        #     if n == 1:
        #         return [1]
        #     elif n == 2:
        #         return [1,1]

        #     dct[n] = [1] + [dct[n-1][i]+dct[n-1][i+1] for i in range(n-2)] + [1]
        #     return dct[n]
        # return [gen(i, dct) for i in range(1, numRows+1)]
        
        
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        
        result = [[1], [1,1]]
        for i in range(3, numRows+1):
            result.append([1]+[result[i-2][j]+result[i-2][j+1] for j in range(i-2)]+[1])
        return result

# @lc code=end

