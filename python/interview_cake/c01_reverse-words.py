"""
You're working on a secret team solving coded transmissions.

Your team is scrambling to decipher a recent message, worried it's a plot to break into a major European National Cake Vault. The message has been mostly deciphered, but all the words are backward! Your colleagues have handed off the last step to you.

Write a function reverse_words() that takes a message as a list of characters and reverses the order of the words in place.

Assume the message contains only letters and spaces, and all words are separated by one space.

Time: O(n)
Space: O(1)
"""


def reverse_words(words: list[str]):
    reverse_range(words, 0, len(words) - 1)
    p = 0
    for i in range(len(words)):
        if words[i] == " ":
            reverse_range(words, p, i - 1)
            p = i + 1
    reverse_range(words, p, len(words) - 1)


def reverse_range(string: list[str], p1: int, p2: int):
    while p1 < p2:
        string[p1], string[p2] = string[p2], string[p1]
        p1 += 1
        p2 -= 1


cases = (
    (
        ["c", "a", "k", "e", " ", "o", "n", "e", " ", "s", "t", "e", "a", "l"],
        ["s", "t", "e", "a", "l", " ", "o", "n", "e", " ", "c", "a", "k", "e"],
    ),
    (
        ["w", "o", "r", "l", "d", " ", "h", "e", "l", "l", "o"],
        ["h", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d"],
    ),
    (
        ["p", "r", "o", "b", "l", "e", "m", " ", "e", "a", "s", "y"],
        ["e", "a", "s", "y", " ", "p", "r", "o", "b", "l", "e", "m"],
    ),
)
for words, want in cases:
    reverse_words(words)
    assert words == want, f"got: {words}, want: {want}"
