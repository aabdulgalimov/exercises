"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Constraints:
    n == height.length
    1 <= n <= 2 * 10^4
    0 <= height[i] <= 10^5

Time: O(n)
Space: O(1)
"""


def trap(height: list[int]) -> int:
    total = 0
    max_left = height[0]
    max_right = height[len(height) - 1]
    left = 1
    right = len(height) - 2
    while left <= right:
        if max_left < max_right:
            if height[left] > max_left:
                max_left = height[left]
            else:
                total += max_left - height[left]
            left += 1
        else:
            if height[right] > max_right:
                max_right = height[right]
            else:
                total += max_right - height[right]
            right -= 1
    return total


cases = (
    # ■
    # ■ ■
    # ■ ■ ■
    # ■ ■ ■ x ■
    ([4, 3, 2, 0, 1], 1),
    #               ■
    #       ■ x x x ■ ■ x ■
    # _ ■ x ■ ■ x ■ ■ ■ ■ ■ ■
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    #           ■
    # ■ x x x x ■
    # ■ x x ■ x ■
    # ■ ■ x ■ ■ ■
    # ■ ■ x ■ ■ ■
    ([4, 2, 0, 3, 2, 5], 9),
    #   ■
    # _ ■ x ■ _
    ([0, 2, 0, 1, 0], 1),
    #     ■
    # _ ■ ■
    ([0, 1, 2], 0),
    # ■
    # ■ ■ _
    ([2, 1, 0], 0),
    # ■
    # ■
    # ■ x ■
    # ■ ■ ■ ■ _
    ([4, 1, 2, 1, 0], 1),
    #                     ■ x ■
    #                     ■ ■ ■
    #           ■ x x x x ■ ■ ■
    # ■ x x x ■ ■ ■ x x x ■ ■ ■
    # ■ x ■ x ■ ■ ■ ■ x ■ ■ ■ ■
    ([2, 0, 1, 0, 2, 3, 2, 1, 0, 1, 5, 4, 5], 14),
    ([0], 0),
)
for height, want in cases:
    got = trap(height)
    assert got == want, f"got: {got}, want: {want} ({height})"
