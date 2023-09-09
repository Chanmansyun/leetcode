#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        for i in s:
            if dict.get(i):
                dict[i] += 1
            else:
                dict[i] = 1
        for j in t:
            if not dict.get(j):
                return False
            else:
                dict[j] -= 1
                if dict[j] == 0:
                    del dict[j]
        if not len(dict):
            return True
        else:
            return False
# @lc code=end

