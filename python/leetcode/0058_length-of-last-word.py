"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Constraints:
    1 <= s.length <= 10^4
    s consists of only English letters and spaces ' '.
    There will be at least one word in s.

Time: O(n)
Space: O(1)
"""


def length_of_last_word(s: str) -> int:
    end = len(s) - 1
    while end > 0 and s[end] == " ":
        end -= 1
    start = end
    while start > -1 and s[start] != " ":
        start -= 1
    return end - start


cases = (
    ("Hello World", 5),
    ("   fly me   to   the moon  ", 4),
    ("luffy is still joyboy", 6),
    ("exercise", 8),
    ("   ", 0),
)
for s, want in cases:
    got = length_of_last_word(s)
    assert got == want, f"got: {got}, want: {want} ({s})"
