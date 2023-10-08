"""
I want to learn some big words so people think I'm smart.

I opened up a dictionary to a page in the middle and started flipping through, looking for words I didn't know. I put each word I didn't know at increasing indices in a huge list I created in memory. When I reached the end of the dictionary, I started from the beginning and did the same thing until I reached the page I started at.

Now I have a list of words that are mostly alphabetical, except they start somewhere in the middle of the alphabet, reach the end, and then start from the beginning of the alphabet. In other words, this is an alphabetically ordered list that has been "rotated".

Write a function for finding the index of the "rotation point," which is where I started working from the beginning of the dictionary. This list is huge so we want to be efficient here.

Time: O(lg n)
Space: O(1)
"""


def find_rotation_point(words: list[str]) -> int:
    start = 0
    end = len(words) - 1
    while start < end:
        middle = start + (end - start) // 2
        if words[middle] < words[0]:
            end = middle - 1
        else:
            start = middle + 1
    point = end + 1
    return point if point != len(words) else 0


cases = (
    (["a", "b", "c", "d", "e", "f"], 0),
    (
        [
            "ptolemaic",
            "retrograde",
            "supplant",
            "undulate",
            "xenoepist",
            "asymptote",  # rotation point
            "babka",
            "banoffee",
            "engender",
            "karpatka",
            "othellolagkage",
        ],
        5,
    ),
)
for words, want in cases:
    got = find_rotation_point(words)
    assert got == want, f"got: {got}, want: {want} ({words})"
