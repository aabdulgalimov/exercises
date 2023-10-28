"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Constraints:
    1 <= haystack.length, needle.length <= 104
    haystack and needle consist of only lowercase English characters.

Time: O(n*m)
Space: O(1)
"""


def find_substring(haystack: str, needle: str) -> int:
    if needle == "":
        return 0

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i] == needle[0]:
            for j in range(1, len(needle)):
                if needle[j] != haystack[i + j]:
                    break
            else:
                return i

    return -1


# pythonic O(n)
def find_substring2(haystack: str, needle: str) -> int:
    try:
        return haystack.index(needle)
    except ValueError:
        return -1


cases = (
    ("sadbutsad", "sad", 0),
    ("leetcode", "leeto", -1),
    ("aaa", "aaaa", -1),
    ("a", "a", 0),
    ("a", "", 0),
)
for haystack, needle, want in cases:
    got = find_substring(haystack, needle)
    assert got == want, f"got: {got}, want: {want} ({haystack} {needle})"
