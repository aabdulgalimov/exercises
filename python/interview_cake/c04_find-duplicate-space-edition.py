"""
We have a list of integers, where:
    The integers are in the range 1..n
    The list has a length of n+1

It follows that our list has at least one integer which appears at least twice. But it may have several duplicates, and each duplicate may appear more than twice.

Write a function which finds an integer that appears more than once in our list. (If there are multiple duplicates, you only need to find one of them.)
Optimize for space.

Time: O(n*lg n)
Space: O(1)
"""


def find_duplicate(ints: list[int]) -> int:
    start = 1
    end = len(ints) - 1
    while start < end:
        middle = start + (end - start) // 2
        lower_range_start, lower_range_end = start, middle
        upper_range_start, upper_range_end = middle + 1, end
        lower_count = 0
        for i in ints:
            if i >= lower_range_start and i <= lower_range_end:
                lower_count += 1
        if lower_count > (lower_range_end - lower_range_start + 1):
            start, end = lower_range_start, lower_range_end
        else:
            start, end = upper_range_start, upper_range_end
    return start


cases = (
    ([1, 1, 2, 3], 1),
    ([1, 2, 2, 3], 2),
    ([1, 2, 3, 3], 3),
    ([1, 2, 3, 4, 5, 1], 1),
    ([1, 2, 3, 3, 3, 4, 5, 5], 3),
    ([1, 1, 1, 1, 5, 5], 1),
)
for ints, want in cases:
    got = find_duplicate(ints)
    assert got == want, f"got: {got}, want: {want} ({ints})"
