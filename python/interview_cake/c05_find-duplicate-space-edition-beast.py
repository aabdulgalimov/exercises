"""
We have a list of integers, where:
    The integers are in the range 1..n
    The list has a length of n+1

It follows that our list has at least one integer which appears at least twice. But it may have several duplicates, and each duplicate may appear more than twice.

Write a function which finds an integer that appears more than once in our list. (If there are multiple duplicates, you only need to find one of them.)
Optimize for space.
Imagine each item in the list as a node in a linked list to get O(n) time.

Time: O(n)
Space: O(1)
"""


def find_duplicate(ints):
    n = len(ints) - 1

    # get inside a cycle
    position_in_cycle = n + 1
    for _ in range(n):
        position_in_cycle = ints[position_in_cycle - 1]

    # find cycle length
    start = position_in_cycle
    p = ints[start - 1]
    cycle_length = 1
    while p != start:
        p = ints[p - 1]
        cycle_length += 1

    # find first node of the cycle (duplicate value)
    p1 = n + 1
    p2 = p1
    for _ in range(cycle_length):
        p2 = ints[p2 - 1]
    while p1 != p2:
        p1 = ints[p1 - 1]
        p2 = ints[p2 - 1]

    return p1


cases = (
    ([1, 1, 2, 3], 1),
    ([1, 2, 2, 3], 2),
    ([1, 2, 3, 3], 3),
    ([1, 2, 3, 4, 5, 1], 1),
    ([1, 2, 3, 3, 3, 4, 5, 7], 3),
    ([1, 1, 1, 1, 5, 5], 5),
    ([4, 1, 4, 2, 3], 4),
)
for ints, want in cases:
    got = find_duplicate(ints)
    assert got == want, f"got: {got}, want: {want} ({ints})"
