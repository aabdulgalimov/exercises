"""
Write a function to validate that a given string has the correct opener/closer bracket sequence ("[]", "()", "{}", "||").
A closer is valid if and only if it's the closer for the most recently seen, unclosed opener.

Time: O(n)
Space: O(n)
"""


def validate(s: str) -> bool:
    brackets: list[str] = []
    bar_count = 0
    for c in s:
        if c in ("(", "{", "["):
            brackets.append(c)
        elif c == ")":
            if not brackets or brackets.pop() != "(":
                return False
        elif c == "}":
            if not brackets or brackets.pop() != "{":
                return False
        elif c == "]":
            if not brackets or brackets.pop() != "[":
                return False
        elif c == "|":
            if bar_count:
                if not brackets or brackets.pop() != "|":
                    return False
                bar_count -= 1
            else:
                brackets.append(c)
                bar_count = 1
    return not brackets


cases = (
    ("Test ( {test} [ ()]) .", True),
    ("([]", False),
    ("(|||{[]}|||) ||", True),
)
for s, want in cases:
    got = validate(s)
    assert got == want, f"got: {got}, want: {want} ({s})"
