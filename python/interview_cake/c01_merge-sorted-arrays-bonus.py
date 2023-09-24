"""
What if we wanted to merge several sorted lists? Write a function that takes as an input a list of sorted lists and outputs a single sorted list with all the items from each list.

Do we absolutely have to allocate a new list to use for the merged output? Where else could we store our merged list? How would our function need to change?

Time: O(n)
Space: O(1)
"""
from typing import Generator


def merge_lists(lists: list[list[int]]) -> Generator[int, None, None]:
    pointers = [0] * len(lists)
    item_count = sum(len(l) for l in lists)
    done = 0
    while done < item_count:
        i = min(
            (i for i, p in enumerate(pointers) if p < len(lists[i])),
            key=lambda x: lists[x][pointers[x]],
        )
        yield lists[i][pointers[i]]
        pointers[i] += 1
        done += 1


cases = (
    ([[1]], [1]),
    ([[1], [2]], [1, 2]),
    ([[3, 5, 6], [1, 4], [2]], [1, 2, 3, 4, 5, 6]),
)
for lists, want in cases:
    got = list(merge_lists(lists))
    assert got == want, f"got: {got}, want: {want} ({lists})"
