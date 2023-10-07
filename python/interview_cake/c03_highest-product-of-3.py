"""
Given a list of integers, find the highest product you can get from three of the integers.

Constraints:
    The input list_of_ints will always have at least three integers.
    Integers can be negative.

Time: O(n)
Space: O(1)
"""


def highest_product(ints: list[int]) -> int:
    result = ints[0] * ints[1] * ints[2]
    highest_product_2 = ints[0] * ints[1]
    lowest_product_2 = highest_product_2
    highest = max(ints[0], ints[1])
    lowest = min(ints[0], ints[1])
    for i in range(2, len(ints)):
        n = ints[i]
        result = max(result, n * highest_product_2, n * lowest_product_2)
        highest_product_2 = max(highest_product_2, n * highest, n * lowest)
        lowest_product_2 = min(lowest_product_2, n * highest, n * lowest)
        highest = max(highest, n)
        lowest = min(lowest, n)
    return result


cases = (
    ([1, 1, 1], 1),
    ([1, 1, 1, 2, 3], 6),
    ([2, 2, 2, 1, 1, 1, 3], 12),
    ([-5, 1, 1, 1], 1),
    ([-5, -1, 1, 1], 5),
    ([-1, -1, -1, 1], 1),
)
for ints, want in cases:
    got = highest_product(ints)
    assert got == want, f"got: {got}, want: {want} ({ints})"
