"""
Writing programming interview questions hasn't made me rich yet ... so I might give up and start trading Apple stocks all day instead.
First, I wanna know how much money I could have made yesterday if I'd been trading Apple stocks all day.
So I grabbed Apple's stock prices from yesterday and put them in a list called stock_prices, where:
    - The indices are the time (in minutes) past trade opening time, which was 9:30am local time.
    - The values are the price (in US dollars) of one share of Apple stock at that time.
So if the stock cost $500 at 10:30am, that means stock_prices[60] = 500.

Write a function that takes stock_prices and returns the best profit I could have made from one purchase and one sale of one share of Apple stock yesterday.
No "shorting" - you need to buy before you can sell. Also, you can't buy and sell in the same time step - at least 1 minute has to pass.

Time: O(n)
Space: O(1)
"""


def find_max_profit(prices: list[int]) -> int:
    if len(prices) < 2:
        raise ValueError("finding a profit requires at least 2 prices")

    max_profit = prices[1] - prices[0]
    min_buy = min(prices[0], prices[1])
    for i in range(2, len(prices)):
        max_profit = max(max_profit, prices[i] - min_buy)
        min_buy = min(min_buy, prices[i])

    return max_profit


cases = (
    ([10, 7, 5, 8, 11, 9], 6),
    ([3, 2, 1], -1),
    ([7, 2, 1], -1),
)
for prices, want in cases:
    got = find_max_profit(prices)
    assert got == want, f"got: {got}, want: {want} ({prices})"
