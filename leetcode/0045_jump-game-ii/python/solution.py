"""
You are given an array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
    0 <= j <= nums[i] and i + j < n

Return the minimum number of jumps to reach nums[n - 1].

Constraints:
    1 <= nums.length <= 10^4
    0 <= nums[i] <= 1000
    It's guaranteed that you can reach nums[n - 1].

Time: O(n)
Space: O(1)
"""


def jump(nums: list[int]) -> int:
    jump_count = 0
    p = 0
    max_p = nums[0]
    last_i = len(nums) - 1
    while p < last_i:
        jump_count += 1
        if max_p >= last_i:
            break
        else:
            new_max_p = max(i + nums[i] for i in range(p, max_p + 1))
            p, max_p = max_p, new_max_p
    return jump_count


cases = (
    ([2, 3, 1, 1, 4], 2),
    ([2, 3, 0, 1, 4], 2),
)
for nums, want in cases:
    got = jump(nums)
    assert got == want, f"got: {got}, want: {want} ({nums})"
