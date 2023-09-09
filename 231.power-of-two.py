#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n == 1:
        #     return True
        # elif n % 2 != 0 or n <= 0:            
        #     return False
        
        # pow = 1
        # while 2**pow < n:
        #     pow += 1
        #     if 2**pow > n:
        #         return False
        #     elif 2**pow == n:
        #         return True
        # return True
        return n>0 and n & (n-1) == 0
# @lc code=end

