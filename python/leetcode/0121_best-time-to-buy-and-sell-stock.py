"""
You are given an array prices where prices[i] is the price of a given stock on the i-th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Constraints:
    1 <= prices.length <= 10^5
    0 <= prices[i] <= 10^4

Time: O(n)
Space: O(1)
"""


def max_profit(prices: list[int]) -> int:
    profit = 0
    min_price = prices[0]
    for i in range(1, len(prices)):
        price = prices[i]
        new_profit = price - min_price
        if new_profit > profit:
            profit = new_profit
        if price < min_price:
            min_price = price
    return profit


prices = [7, 8, 3, 6, 4]
print(max_profit(prices))
