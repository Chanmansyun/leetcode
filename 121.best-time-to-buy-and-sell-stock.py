#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0
        for i in range(len(prices)):
            if profit < prices[i] - min_price:
                profit = prices[i] - min_price
            if min_price > prices[i]:
                min_price = prices[i]
        return profit

                
# @lc code=end

