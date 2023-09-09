#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = s[0]
        for i in range(len(s)-1):
            temp = ""
            if i-1>=0 and s[i-1] == s[i+1]:
                temp = s[i-1:i+2]
                j = 2
                while i-j>=0 and i+j<=len(s)-1:
                    if s[i-j] == s[i+j]:
                        temp = s[i-j] + temp + s[i+j]
                        j += 1
                        continue
                    else:
                        break
                if len(temp) > len(result):
                    result = temp
            if s[i] == s[i+1]:
                temp = s[i]+s[i+1]
                j = 1
                while i-j>=0 and i+1+j<len(s):
                    if s[i-j] == s[i+j+1]:
                        temp = s[i-j] + temp + s[i+1+j] 
                        j += 1
                        continue
                    else:
                        break
                if len(temp) > len(result):
                    result = temp
        return result
# @lc code=end

