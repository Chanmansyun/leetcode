#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        
        while True:
            result = 0
            for i in str(num):
                result += int(i)
            if result < 10:
                return result
            num = result
# @lc code=end

