"""
There is a list of n+1 numbers. Every number in the range 1..n appears once except for one number that appears twice.
Write a function for finding the number that appears twice.

Time: O(n)
Space: O(1)
"""


def find_duplicate(nums: list[int]) -> int:
    n = len(nums) - 1
    series_sum = (n * n + n) / 2  # triangular series sum
    actual_sum = sum(nums)
    return actual_sum - series_sum


cases = (
    ([3, 1, 3, 4, 2], 3),
    ([1, 1], 1),
)
for nums, want in cases:
    got = find_duplicate(nums)
    assert got == want, f"got: {got}, want: {want} ({nums})"
