"""
Write a function that checks whether one string is an anagram of another.
Anagram is a string formed by rearranging the characters of another string.

Input:
    Two strings on separate lines. Strings contain only latin letters and are no longer than 10^5 characters.

Output:
    "YES" or "NO".

Time: O(n)
Space: O(1)
"""
import io
from contextlib import redirect_stdout
from unittest.mock import patch
from collections import defaultdict


def solution():
    s1 = input()
    s2 = input()
    counts1 = defaultdict(int)
    counts2 = defaultdict(int)
    for c in s1:
        counts1[c] += 1
    for c in s2:
        counts2[c] += 1

    for c, count in counts1.items():
        if count != counts2.get(c, 0):
            print("NO")
            break
    else:
        print("YES")


cases = (
    (["dusty", "study"], "YES"),
    (["rat", "bat"], "NO"),
)
for data, want in cases:
    with patch("builtins.input", side_effect=data):
        with redirect_stdout(io.StringIO()) as f:
            solution()
            got = f.getvalue()[:-1]
            assert got == want, f"got: {got}, want: {want} ({data})"
