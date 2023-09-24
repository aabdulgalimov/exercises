"""
In order to win the prize for most cookies sold, my friend Alice and I are going to merge our Girl Scout Cookies orders and enter as one unit.

Each order is represented by an "order id" (an integer).

We have our lists of orders sorted numerically already, in lists. Write a function to merge our lists of orders into one sorted list.

Time: O(n)
Space: O(n)
"""


def merge_lists(list1: list[int], list2: list[int]) -> list[int]:
    result = [0] * (len(list1) + len(list2))
    p1, p2 = 0, 0
    for i in range(len(result)):
        if p1 < len(list1) and (p2 >= len(list2) or list1[p1] < list2[p2]):
            result[i] = list1[p1]
            p1 += 1
        else:
            result[i] = list2[p2]
            p2 += 1
    return result


cases = (
    ([1, 2, 4], [3], [1, 2, 3, 4]),
    (
        [3, 4, 6, 10, 11, 15],
        [1, 5, 8, 12, 14, 19],
        [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19],
    ),
)
for list1, list2, want in cases:
    got = merge_lists(list1, list2)
    assert got == want, f"got: {got}, want: {want} ({list1} {list2})"
