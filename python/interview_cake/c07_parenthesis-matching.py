"""
Write a function that, given a sentence along with the position of an opening parenthesis, finds the corresponding closing parenthesis.

Time: O(n)
Space: O(1)
"""


def find_closing_bracket(s: str, p: int) -> int | None:
    to_close = 1
    for i in range(p + 1, len(s)):
        c = s[i]
        if c == "(":
            to_close += 1
        elif c == ")":
            to_close -= 1
            if to_close == 0:
                return i


cases = (
    ("Test ( (test) ( ())) .", 5, 19),
    ("(()", 0, None),
)
for s, p, want in cases:
    got = find_closing_bracket(s, p)
    assert got == want, f"got: {got}, want: {want} ({s} {p})"
