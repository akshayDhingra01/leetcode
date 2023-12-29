# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


# Optimized Solution || Time O(N) || Space O(1) || Two Pointers || Sliding window

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_side = prices[0]
        max_profit = 0

        for price in prices[1:]:
            if price < min_side:
                min_side = price
            if price > min_side:
                max_profit = max(price - min_side, max_profit)       

        return max_profit
