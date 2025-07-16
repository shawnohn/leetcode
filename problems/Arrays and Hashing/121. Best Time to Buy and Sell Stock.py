# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150
# Difficulty: Easy
# Tag: Array, Dynamic Programming

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for sell in prices[1:]:
            if sell > buy:
                profit = max(profit, sell - buy)
            else:
                buy = sell
        return profit


# Solution
# O(n) time | O(1) space
# Iterate through from the second day.
# If the current price is greater than the buy price, we can make a profit, so update the maximum profit by comparing the current profit and the new profit.
# If the current price is less than the buy price, update the buy price.
# Return the maximum profit.
