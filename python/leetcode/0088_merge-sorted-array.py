"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored.

Constraints:
    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -10^9 <= nums1[i], nums2[j] <= 10^9

Time: O(n+m)
Space: O(1)
"""


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    i1 = m - 1
    i2 = n - 1
    pos = m + n - 1
    while i2 >= 0:
        if i1 >= 0 and nums1[i1] > nums2[i2]:
            nums1[pos] = nums1[i1]
            i1 -= 1
        else:
            nums1[pos] = nums2[i2]
            i2 -= 1
        pos -= 1


cases = (
    ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
    ([1], 1, [], 0, [1]),
    ([0], 0, [1], 1, [1]),
)
for nums1, m, nums2, n, want in cases:
    merge(nums1, m, nums2, n)
    assert nums1 == want, f"got: {nums1}, want: {want} ({nums2} {n})"
