# problem:
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# solution:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price,max_profit = float('inf'),0
        for price in prices:
            min_price = min(price,min_price)
            profit = price-min_price
            max_profit = max(max_profit,profit)
        return max_profit