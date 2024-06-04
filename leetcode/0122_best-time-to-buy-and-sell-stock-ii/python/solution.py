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


cases = (
    ([7, 1, 5, 3, 6, 4], 7),
    ([1, 2, 3, 4, 5], 4),
    ([7, 6, 4, 3, 1], 0),
)
for prices, want in cases:
    got = max_profit(prices)
    assert got == want, f"got: {got}, want: {want} ({prices})"
