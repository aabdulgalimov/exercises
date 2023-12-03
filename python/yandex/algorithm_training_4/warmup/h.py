"""
To evaluate quality of programming training, each student group has one metric - the total number of solved problems.
The total number of solved problems in the first group is equal a and in the second group - b.
n unique problems were present at the contest and each student solved at least 1 problem (and at most n).

Find whether the first group could have more students than the second.

Input:
    Integers a, b and n on separate lines (1 ≤ a, b, n ≤ 10^4).

Output:
    "Yes" or "No".

Time: O(1)
Space: O(1)
"""
import math
import io
from contextlib import redirect_stdout
from unittest.mock import patch


def solution():
    a, b, n = int(input()), int(input()), int(input())
    print("Yes" if a > math.ceil(b / n) else "No")


cases = (
    (["60", "30", "4"], "Yes"),
    (["30", "30", "1"], "No"),
    (["30", "150", "4"], "No"),
    (["30", "119", "4"], "No"),
    (["30", "120", "4"], "No"),
    (["31", "120", "4"], "Yes"),
    (["31", "123", "4"], "No"),
)
for data, want in cases:
    with patch("builtins.input", side_effect=data):
        with redirect_stdout(io.StringIO()) as f:
            solution()
            got = f.getvalue()[:-1]
            assert got == want, f"got: {got}, want: {want} ({data})"
