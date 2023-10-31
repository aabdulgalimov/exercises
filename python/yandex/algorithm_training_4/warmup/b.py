"""
Add two rational fractions a/b and c/d and print the result as an irreducible fraction m/n.

Constraints:
    1 <= a,b,c,d <= 100

Time: O(1)
Space: O(1)
"""
import io
from contextlib import redirect_stdout
from unittest.mock import patch


def solution():
    a, b, c, d = (int(x) for x in input().split())
    m = a * d + c * b
    n = b * d
    r1, r2 = m, n
    while r1 and r2:
        if r1 > r2:
            r1 %= r2
        else:
            r2 %= r1
    gcd = r1 or r2
    print(m // gcd, n // gcd)


cases = (
    ("1 2 1 2", "1 1"),
    ("1 4 2 3", "11 12"),
    ("1 5 2 5", "3 5"),
)
for fractions, want in cases:
    with patch("builtins.input", side_effect=[fractions]):
        with redirect_stdout(io.StringIO()) as f:
            solution()
            got = f.getvalue()[:-1]
            assert got == want, f"got: {got}, want: {want} ({fractions})"
