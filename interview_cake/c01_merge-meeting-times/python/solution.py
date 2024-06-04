"""
Your company built an in-house calendar tool called HiCal. You want to add a feature to see the times in a day when everyone is available.

To do this, you'll need to know when any team is having a meeting. In HiCal, a meeting is stored as a tuple of integers (start_time, end_time). These integers represent the number of 30-minute blocks past 9:00am.
For example:
    (2, 3)  # Meeting from 10:00 - 10:30 am
    (6, 9)  # Meeting from 12:00 - 1:30 pm

Write a function merge_ranges() that takes a list of multiple meeting time ranges and returns a list of condensed ranges.

Do not assume the meetings are in order. The meeting times are coming from multiple teams.
The solution must be efficient even when we can't put an upper bound on the numbers representing our time ranges.

Time: O(n*lg n)
Space: O(n)
"""


def merge_ranges(ranges: list[tuple[int]]) -> list[tuple[int]]:
    sorted_ranges = sorted(ranges)
    result = [sorted_ranges[0]]
    for i in range(1, len(sorted_ranges)):
        start, end = sorted_ranges[i]
        last_start, last_end = result[-1]
        if end > last_end:
            if start <= last_end:
                result[-1] = (last_start, end)
            else:
                result.append(sorted_ranges[i])
    return result


cases = (
    ([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)], [(0, 1), (3, 8), (9, 12)]),
    ([(3, 5), (0, 2), (2, 3)], [(0, 5)]),
    ([(0, 3), (1, 2)], [(0, 3)]),
    ([(0, 1), (2, 3), (1, 2)], [(0, 3)]),
    ([(0, 1), (0, 1)], [(0, 1)]),
)
for ranges, want in cases:
    got = merge_ranges(ranges)
    assert got == want, f"got: {got}, want: {want} ({ranges})"
