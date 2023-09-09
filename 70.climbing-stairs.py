#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        dct = {1:1, 2:2}
        def cs(n, dct):
            if dct.get(n):
                return dct.get(n)
            if dct.get(n-1):
                last_one = dct.get(n-1)
            else:
                last_one = cs(n-1, dct)
                dct[n-1] = last_one
            
            if dct.get(n-2):
                last_two = dct.get(n-2)
            else:
                last_two = cs(n-2, dct)
                dct[n-2] = last_two
            return last_one + last_two     
            # dct[n] = cs(n-1, dct) + cs(n-2, dct)                                
            # return dct[n]
        return cs(n, dct)
# @lc code=end

