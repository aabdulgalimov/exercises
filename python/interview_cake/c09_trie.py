"""
I wrote a crawler that visits web pages, stores a few keywords in a database, and follows links to other web pages.
I noticed that my crawler was wasting a lot of time visiting the same pages over and over, so I made a set "visited" where I'm storing URLs I've already visited.
Now the crawler only visits a URL if it hasn't already been visited.

Thing is, the crawler is running on my old desktop computer and it keeps running out of memory because visited is getting so huge.
How can I trim down the amount of space taken up by visited?

Answer: replace a set with a trie (search tree)
"""


class Trie(object):
    def __init__(self):
        self.root: dict = {}

    def add_url(self, url) -> bool:
        is_new = False
        node = self.root

        for c in url:
            if c not in node:
                is_new = True
                node[c] = {}
            node = node[c]

        if "|" not in node:  # end of word
            is_new = True
            node["|"] = {}

        return is_new
