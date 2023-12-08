"""
Write a function that, given an amount of money and a list of coin denominations, computes the number of ways to make the amount of money with coins of the available denominations.

Time: O(n*m)
Space: O(n)
"""


def count_combinations(amount: int, coins: list[int]) -> int:
    options = [0] * (amount + 1)
    options[0] = 1  # only one option of making 0 amount
    for coin in coins:
        for sub_amount in range(coin, amount + 1):
            options[sub_amount] += options[sub_amount - coin]
    return options[amount]


cases = (
    (4, [1, 2, 3], 4),
    (1, [1], 1),
    (1, [2], 0),
    (5, [2, 3], 1),
    (6, [2, 3], 2),
)
for amount, coins, want in cases:
    got = count_combinations(amount, coins)
    assert got == want, f"got: {got}, want: {want} ({amount} {coins})"
