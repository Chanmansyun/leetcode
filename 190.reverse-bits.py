#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:][::-1]
        if len(n) < 32:
            n += "0"*(32-len(n))
        return int(n, 2)
        
# @lc code=end

