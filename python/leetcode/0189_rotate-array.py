"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Constraints:
    1 <= nums.length <= 10^5
    -2^31 <= nums[i] <= 2^31 - 1
    0 <= k <= 10^5

Time: O(n)
Space: O(1)
"""


def rotate(nums: list[int], k: int) -> None:
    def reverse(nums: list[int], i1: int, i2: int) -> None:
        while i1 < i2:
            tmp = nums[i1]
            nums[i1] = nums[i2]
            nums[i2] = tmp
            i1 += 1
            i2 -= 1

    k %= len(nums)
    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)


# pythonic alternative with O(n) space
def rotate2(nums: list[int], k: int) -> None:
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]


cases = (
    ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
    ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
)
for nums, k, want in cases:
    rotate(nums, k)
    assert nums == want, f"got: {nums}, want: {want} ({k})"
