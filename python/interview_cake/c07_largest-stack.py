"""
Implement a stack class "MaxStack" which in addition to default push/pop/peek operations has an additional get_max method that returns the largest item from the stack without removing it.
Assume that the stack will only contain integers.

Time: O(1) for all methods
Space: O(n)
"""


class MaxStack:
    def __init__(self) -> None:
        self.items: list[int] = []
        self.max_items: list[int] = []

    def push(self, item) -> None:
        self.items.append(item)
        if not self.max_items or item >= self.max_items[-1]:
            self.max_items.append(item)

    def pop(self) -> int | None:
        try:
            item = self.items.pop()
            if item == self.max_items[-1]:
                self.max_items.pop()
            return item
        except IndexError:
            return None

    def peek(self) -> int | None:
        try:
            return self.items[-1]
        except IndexError:
            return None

    def get_max(self) -> int | None:
        try:
            return self.max_items[-1]
        except IndexError:
            return None


cases = (
    (1, [], None),
    (2, ["s.push(1)", "s.push(3)", "s.pop()", "s.push(0)"], 1),
)
for case, ops, want in cases:
    s = MaxStack()
    for op in ops:
        exec(op)
    got = s.get_max()
    assert got == want, f"got: {got}, want: {want} ({case})"
