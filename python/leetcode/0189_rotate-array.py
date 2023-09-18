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


# cyclic O(n) & O(1)
def rotate2(nums: list[int], k: int) -> None:
    k %= len(nums)
    count = 0
    start = 0
    while count < len(nums):
        last_pos = start
        last_item = nums[start]

        while True:
            next_pos = (last_pos + k) % len(nums)

            temp = nums[next_pos]
            nums[next_pos] = last_item
            last_item = temp

            count += 1
            last_pos = next_pos
            if start == last_pos:
                break

        start += 1


# pythonic O(n) & O(n)
def rotate3(nums: list[int], k: int) -> None:
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print(nums)
