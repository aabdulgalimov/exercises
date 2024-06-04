"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Constraints:
    2 <= nums.length <= 10^4
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
    Only one valid answer exists.

Time: O(n)
Space: O(n)
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    m = dict()
    for i, n in enumerate(nums):
        j = m.get(target - n)
        if j is not None:
            return [i, j]
        m[n] = i


cases = (
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
)
for nums, target, want in cases:
    got = two_sum(nums, target)
    assert set(got) == set(want), f"got: {got}, want: {want} ({nums} {target})"
