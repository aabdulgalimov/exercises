"""
Write a recursive function for generating all permutations of an input string. Return them as a set.
Assume every character in the input string is unique.

Time: O(n!)
Space: O(n*n!)
"""


def get_permutations(s: str) -> set[str]:
    if len(s) <= 1:
        return set([s])

    permutations = set()
    for p in get_permutations(s[1:]):
        for i in range(len(s)):
            permutations.add(p[:i] + s[0] + p[i:])

    return permutations


cases = (
    ("", set([""])),
    ("ab", set(["ab", "ba"])),
    ("abc", set(["abc", "acb", "bac", "bca", "cab", "cba"])),
)
for s, want in cases:
    got = get_permutations(s)
    assert got == want, f"got: {got}, want: {want} ({s})"
