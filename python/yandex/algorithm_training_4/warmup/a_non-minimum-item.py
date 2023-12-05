"""
Find any non-minimum item in a given range within a sequence of integers. Return "NOT FOUND" if such item doesn't exist.

Input:
    First line contains two integers N and M, where 1 ≤ N ≤ 100 and 1 ≤ M ≤ 1000 - length of the sequence and amount of queries (ranges).
    Second line - the sequence.
    Starting from the third line - M requests with ranges L-R (each on a separate line), where L and R are zero-based indexes of the sequence.

Output:
    M lines, each containing a non-minimum item in a requested range or a string "NOT FOUND" if no such item exists.

Time: O(n)
Space: O(1)
"""
import io
from contextlib import redirect_stdout
from unittest.mock import patch


def solution():
    m = int(input().split()[1])
    arr = [int(x) for x in input().split()]
    for _ in range(m):
        i1, i2 = [int(x) for x in input().split()]
        for i in range(i1 + 1, i2 + 1):
            if arr[i] < arr[i1]:
                print(arr[i1])
                break
            elif arr[i] > arr[i1]:
                print(arr[i])
                break
        else:
            print("NOT FOUND")


cases = (
    (
        1,
        (
            "10 5",
            "1 1 1 2 2 2 3 3 3 10",
            "0 1",
            "0 3",
            "3 4",
            "7 9",
            "3 7",
        ),
        ["NOT FOUND", "2", "NOT FOUND", "10", "3"],
    ),
    (
        2,
        (
            "4 2",
            "1 1 1 2",
            "0 2",
            "0 3",
        ),
        ["NOT FOUND", "2"],
    ),
)
for case_id, data, want in cases:
    with patch("builtins.input", side_effect=data):
        with redirect_stdout(io.StringIO()) as f:
            solution()
            got = f.getvalue().split("\n")[:-1]
            assert got == want, f"got: {got}, want: {want} ({case_id})"
