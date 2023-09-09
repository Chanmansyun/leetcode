#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:   
        result = 0
        temp = ""
        for i in s:
            if i not in temp:
                temp += i
            elif i in temp:
                if len(temp) > result:
                    result = len(temp)
                temp = temp[temp.index(i)+1:] + i
        else:
            if len(temp) > result:
                result = len(temp)
        return result
# @lc code=end

