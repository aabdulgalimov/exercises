"""
A group of students has n people. The teacher gave a group project. To complete this project students must split up into sub-groups of size a to b.
Find whether it is possible to split up the student group into sub-groups for the project.

Input:
    First line contains number of cases (1 ≤ t ≤ 100).
    Next lines contain 3 integers for each of the cases - group size and sub-group limits (1 ≤ n ≤ 10^9, 1 ≤ a ≤ b ≤ n).

Output:
    "YES" or "NO" for each case on separate lines.

Time: O(1)
Space: O(1)
"""
import io
from contextlib import redirect_stdout
from unittest.mock import patch


def solution():
    for _ in range(int(input())):
        n, a, b = (int(x) for x in input().split())
        print("NO" if n % a > (b - a) * (n // a) else "YES")


cases = (
    (
        ["4", "10 2 3", "11 7 8", "28 4 6", "3 1 2"],
        ["YES", "NO", "YES", "YES"],
    ),
    (["1", "1 1 1"], ["YES"]),
)
for data, want in cases:
    with patch("builtins.input", side_effect=data):
        with redirect_stdout(io.StringIO()) as f:
            solution()
            got = f.getvalue().split("\n")[:-1]
            assert got == want, f"got: {got}, want: {want} ({data})"
