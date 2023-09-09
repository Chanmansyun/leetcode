#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        
        s_low = s.lower()
        i = -1
        for j in s_low:
            if j.isalnum():
                while not s_low[i].isalnum():
                    i -= 1
                if j != s_low[i]:
                    return False
                i -= 1
        
        # for i, j in enumerate(s_pure):
        #     if j != s_pure[-i-1]:
        #         return False
        
        return True

            
# @lc code=end

