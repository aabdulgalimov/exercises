"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

Constraints:
    n == citations.length
    1 <= n <= 5000
    0 <= citations[i] <= 1000

Time: O(n)
Space: O(n)
"""


def h_index(citations: list[int]) -> int:
    arr_len = len(citations)
    counts = [0] * (arr_len + 1)
    for n in citations:
        counts[min(n, arr_len)] += 1

    total = 0
    for i in range(arr_len, -1, -1):
        total += counts[i]
        if total >= i:
            return i
    return 0


cases = (
    ([3, 0, 6, 1, 5], 3),
    ([1, 3, 1], 1),
)
for citations, want in cases:
    got = h_index(citations)
    assert got == want, f"got: {got}, want: {want} ({citations})"
