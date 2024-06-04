"""
Write an efficient function that checks whether any permutation of an input string is a palindrome.

Time: O(n)
Space: O(1) (number of possible characters if limited)
"""


def has_palindrome_permutation(s: str) -> bool:
    odd = set()
    for c in s:
        if c in odd:
            odd.remove(c)
        else:
            odd.add(c)
    return len(odd) < 2


cases = (
    ("civic", True),
    ("ivicc", True),
    ("civil", False),
    ("livci", False),
    ("xxxzzz", False),
    ("xxzzzz", True),
    ("x", True),
    ("xx", True),
)
for s, want in cases:
    got = has_palindrome_permutation(s)
    assert got == want, f"got: {got}, want: {want} ({s})"
