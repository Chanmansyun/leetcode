#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)[2:]
        cnt = 0
        for i in n:
            if i == "1":
                cnt += 1
        return cnt
# @lc code=end

