#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
            len_1, len_2 = len(haystack), len(needle)
            for j in range(len_1-len_2+1):
                if haystack[j:j+len_2] == needle:
                    return j
            return -1
# @lc code=end

