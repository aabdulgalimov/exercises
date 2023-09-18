"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Constraints:
    1 <= prices.length <= 3 * 10^4
    0 <= prices[i] <= 10^4

Time: O(n)
Space: O(1)
"""


def max_profit(prices: list[int]) -> int:
    total_profit = 0
    for i in range(1, len(prices)):
        profit = prices[i] - prices[i - 1]
        if profit > 0:
            total_profit += profit
    return total_profit


prices = [7, 1, 3, 5, 3, 6, 4]
print(max_profit(prices))
