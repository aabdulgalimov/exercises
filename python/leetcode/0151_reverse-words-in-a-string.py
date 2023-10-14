"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Time: O(n)
Space: O(n)
"""


def reverse_words(s: str) -> str:
    return " ".join(reversed(s.split()))


cases = (
    ("the sky is blue", "blue is sky the"),
    ("  hello world  ", "world hello"),
    ("a good   example", "example good a"),
    ("  test  ", "test"),
    ("", ""),
    ("   ", ""),
)
for s, want in cases:
    got = reverse_words(s)
    assert got == want, f"got: {got}, want: {want} ({s})"
