"""
Write a function that takes a list of characters and reverses the letters in place.

Time: O(n)
Space: O(1)
"""


def reverse_string(chars: list[str]):
    p1 = 0
    p2 = len(chars) - 1
    while p1 < p2:
        chars[p1], chars[p2] = chars[p2], chars[p1]
        p1 += 1
        p2 -= 1


cases = (
    (["p", "y", "t", "h", "o", "n"], ["n", "o", "h", "t", "y", "p"]),
    (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
)
for string, want in cases:
    reverse_string(string)
    assert string == want, f"got: {string}, want: {want}"
