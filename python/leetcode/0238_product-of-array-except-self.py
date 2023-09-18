"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

You must write an algorithm that runs in O(n) time and without using the division operation.

Constraints:
    2 <= nums.length <= 10^5
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Time: O(n)
Space: O(1) (result not included)
"""


def product_except_self(nums: list[int]) -> list[int]:
    result = [1] * len(nums)
    for i in range(1, len(nums)):
        result[i] = result[i - 1] * nums[i - 1]
    right = 1
    for i in range(len(nums) - 2, -1, -1):
        right *= nums[i + 1]
        result[i] *= right
    return result


cases = (
    ([1, 2, 3, 4], [24, 12, 8, 6]),
    ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
)
for arr_in, arr_out in cases:
    result = product_except_self(arr_in)
    if result != arr_out:
        print(arr_in)
        print(f"got: {result}, want: {arr_out}")
        break
