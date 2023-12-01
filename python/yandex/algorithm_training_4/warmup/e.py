"""
In a group of n students, each has a rating ai. Students want to choose a leader so that the overall level of group dissatisfaction is minimal.
If student j is chosen, then dissatisfaction of student i is |ai-aj|.

Find the group's level of dissatisfaction for each student as the leader.

Input:
    First line contains the number of students - an integer n (1 ≤ n ≤ 10^5).
    Second line contains student ratings - n integers a1..an in a non-decreasing order, separated by a space.

Output:
    Group dissatisfaction ratings - n integers separated by a space.

Time: O(n)
Space: O(n)
"""
import io
from contextlib import redirect_stdout
from unittest.mock import patch


def solution():
    n = int(input())
    arr = [int(x) for x in input().split()]
    result = [sum(abs(arr[0] - arr[i]) for i in range(1, n))]
    for i in range(1, n):
        delta = arr[i] - arr[i - 1]
        diff = delta * i - delta * (n - i)
        result.append(result[i - 1] + diff)
    print(" ".join(str(x) for x in result))


cases = (
    (["3", "1 3 4"], "5 3 4"),
    (["5", "3 7 8 10 15"], "28 16 15 17 32"),
    (["8", "1 2 4 7 11 16 22 29"], "84 78 70 64 64 74 98 140"),
)
for data, want in cases:
    with patch("builtins.input", side_effect=data):
        with redirect_stdout(io.StringIO()) as f:
            solution()
            got = f.getvalue()[:-1]
            assert got == want, f"got: {got}, want: {want} ({data})"
