"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
    - Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
    - Return k.

Constraints:
    0 <= nums.length <= 100
    0 <= nums[i] <= 50
    0 <= val <= 100

Time: O(n)
Space: O(1)
"""


def remove_element(nums: list[int], val: int) -> int:
    k = 0
    for n in nums:
        if n != val:
            nums[k] = n
            k += 1
    return k


cases = (
    ([3, 2, 2, 3], 3, [2, 2]),
    ([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 4, 0, 3]),
)
for nums, val, want in cases:
    k = remove_element(nums, val)
    got = nums[:k]
    assert set(got) == set(want), f"got: {got}, want: {want} ({nums} {val})"
