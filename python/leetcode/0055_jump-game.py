"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Constraints:
    1 <= nums.length <= 10^4
    0 <= nums[i] <= 10^5

Time: O(n)
Space: O(1)
"""


def can_jump(nums: list[int]) -> bool:
    max_i = 0
    for i, n in enumerate(nums):
        new_i = i + n
        if max_i < new_i:
            max_i = new_i
        elif max_i == i:
            break
    return i + 1 == len(nums)


cases = (
    ([2, 3, 1, 1, 4], True),
    ([3, 2, 1, 0, 4], False),
)
for nums, want in cases:
    got = can_jump(nums)
    assert got == want, f"got: {got}, want: {want} ({nums})"
