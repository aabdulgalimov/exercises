"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:
    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.

Constraints:
    n == ratings.length
    1 <= n <= 2 * 10^4
    0 <= ratings[i] <= 2 * 10^4

Time: O(n)
Space: O(1)
"""


def candy(ratings: list[int]) -> int:
    total = 1
    up, down, peak = 0, 0, 0
    last_r = ratings[0]
    for i in range(1, len(ratings)):
        r = ratings[i]
        if last_r < r:
            up += 1
            down = 0
            peak = up
            total += 1 + up
        elif last_r > r:
            up = 0
            down += 1
            total += 1 + down
            if peak >= down:
                total -= 1
        else:
            up, down, peak = 0, 0, 0
            total += 1
        last_r = r
    return total


cases = (
    ([1, 0, 2], 5),  # [2, 1, 2]
    ([1, 2, 2], 4),  # [1, 2, 1]
    ([1, 1, 1], 3),  # [1, 1, 1]
    ([5, 4, 3, 2, 5], 12),  # [4, 3, 2, 1, 2]
    ([3, 4, 3, 2, 5], 9),  # [1, 3, 2, 1, 2]
    ([1, 2, 3, 4, 1], 11),  # [1, 2, 3, 4, 1]
    ([1, 5, 4, 3, 2, 1], 16),  # [1, 5, 4, 3, 2, 1]
    ([1, 2, 3, 4, 3, 2, 1], 16),  # [1, 2, 3, 4, 3, 2, 1]
    ([4, 3, 3, 2, 1, 5, 5, 2], 14),  # [2, 1, 3, 2, 1, 2, 2, 1]
)

for ratings, want in cases:
    result = candy(ratings)
    if result != want:
        print(ratings)
        print(f"got: {result}, want: {want}")
        break
