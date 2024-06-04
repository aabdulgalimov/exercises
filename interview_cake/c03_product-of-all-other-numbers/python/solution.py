"""
You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.

Write a function that takes a list of integers and returns a list of the products.

Constraints:
    You can't use division in your solution.

Time: O(n)
Space: O(n)
"""


def get_products(ints: list[int]) -> list[int]:
    result = [1] * len(ints)
    for i in range(1, len(ints)):
        result[i] = result[i - 1] * ints[i - 1]
    right = 1
    for i in range(len(ints) - 2, -1, -1):
        right *= ints[i + 1]
        result[i] *= right
    return result


cases = (
    ([1, 7, 3, 4], [84, 12, 28, 21]),
    ([1, 2, 3], [6, 3, 2]),
    ([8, 4, 2], [8, 16, 32]),
    ([0, 1, 2], [2, 0, 0]),
)
for ints, want in cases:
    got = get_products(ints)
    assert got == want, f"got: {got}, want: {want} ({ints})"
