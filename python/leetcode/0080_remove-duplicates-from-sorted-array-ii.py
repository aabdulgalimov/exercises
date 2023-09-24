"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

You must have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Constraints:
    1 <= nums.length <= 3 * 10^4
    -10^4 <= nums[i] <= 10^4
    nums is sorted in non-decreasing order.

Time: O(n)
Space: O(1)
"""


def remove_duplicates(nums: list[int]) -> int:
    if len(nums) < 3:
        return len(nums)

    k = 0
    for i in range(2, len(nums)):
        if nums[i] != nums[k]:
            nums[k + 2] = nums[i]
            k += 1
    return k + 2


cases = (
    ([1, 1, 1, 2, 2, 3], [1, 1, 2, 2, 3]),
    ([0, 0, 1, 1, 1, 1, 2, 3, 3], [0, 0, 1, 1, 2, 3, 3]),
)
for nums, want in cases:
    k = remove_duplicates(nums)
    got = nums[:k]
    assert got == want, f"got: {got}, want: {want} ({nums})"
