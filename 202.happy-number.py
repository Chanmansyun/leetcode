#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 4 and n != 1:
            return False
        
        nums = [n]
        while True:
            square_result = 0
            while n//10:
                square_result += (n%10)**2
                n = n//10
            square_result += (n%10)**2
            
            if square_result == 1:
                return True
            if square_result in nums:
                return False
            nums.append(square_result)
            n = square_result
        
        
# @lc code=end

