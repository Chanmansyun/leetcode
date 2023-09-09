#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_a = {}
        dict_b = {}
        for i, j in zip(s, t):
            if not dict_a.get(i):
                if not dict_b.get(j):
                    dict_a[i] = j
                    dict_b[j] = i
                elif dict_b.get(j) != i:
                    return False
            elif dict_a.get(i) != j:
                return False
        return True
        
        # lt_a = []
        # lt_b = []
        # for i in s:
        #     lt_a.append(s.index(i))
        # for i in t:
        #     lt_b.append(t.index(i))
        # if lt_a == lt_b:
        #     return True
        # else:
        #     return False
                
# @lc code=end

