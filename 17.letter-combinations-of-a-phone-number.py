#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def get(self, digital):
        dict = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        return dict[digital]

    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        for i, j in enumerate(digits):
            temp = self.letterCombinations(digits[i+1:])
            for x in self.get(j):
                if temp:
                    for y in temp:
                        result.append(x + y)
                else:
                    result.append(x)
            return result
# @lc code=end

