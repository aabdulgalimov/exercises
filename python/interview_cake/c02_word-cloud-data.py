"""
You want to build a word cloud, an infographic where the size of a word corresponds to how often it appears in the body of text.

To do this, you'll need data. Write code that takes a long string and builds its word cloud data in a dictionary, where the keys are words and the values are the number of times the words occurred.

Think about capitalized words.
Assume the input will only contain words and standard punctuation.

Time: O(n)
Space: O(n)
"""
import collections


def count_words(s: str) -> dict[str, int]:
    result: dict[str, int] = collections.defaultdict(int)
    p = 0
    for i, c in enumerate(s):
        if not (c.isalpha() or c in ("-", "'")):
            if p < i:
                word = s[p:i]
                if p == 0 or (p > 2 and s[p - 2] == "."):
                    word = word[0].lower() + word[1:]
                result[word] += 1
            p = i + 1
    return result


cases = (
    (
        "We came, we saw, we ate cake.",
        {"we": 3, "came": 1, "saw": 1, "ate": 1, "cake": 1},
    ),
    (
        "We came. We saw. We conquered.",
        {"we": 3, "came": 1, "saw": 1, "conquered": 1},
    ),
    (
        "We failed...then we ate Bill's cake.",
        {"we": 2, "failed": 1, "then": 1, "ate": 1, "Bill's": 1, "cake": 1},
    ),
    (
        "The bill came to five dollars.",
        {"the": 1, "bill": 1, "came": 1, "to": 1, "five": 1, "dollars": 1},
    ),
    ("Check-in.", {"check-in": 1}),
    ("This—rules.", {"this": 1, "rules": 1}),  # em dash
)
for s, want in cases:
    got = count_words(s)
    assert got == want, f"got: {got}, want: {want} ({s})"
