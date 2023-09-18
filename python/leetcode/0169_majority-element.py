"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Constraints:
    n == nums.length
    1 <= n <= 5 * 10^4
    -10^9 <= nums[i] <= 10^9

Time: O(n)
Space: O(1)
"""


def majority_element(nums: list[int]) -> int:
    candidate, count = 0, 0
    for n in nums:
        if count == 0:
            candidate = n
        if n == candidate:
            count += 1
        else:
            count -= 1
    return candidate


nums = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(nums))
