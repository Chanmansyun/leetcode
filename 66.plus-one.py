#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:        
        digits[-1] += 1
        
        idx = len(digits)-1
        while digits[idx] >= 10:
            digits[idx] = digits[idx]%10
            if idx-1 >= 0:
                digits[idx-1] += 1
            else:
                digits = [1] + digits
            idx -= 1
        
        return digits
        
        
# @lc code=end

