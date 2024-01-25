"""
Implement a queue using two stacks.

Time: O(m) where m = number of enqueue/dequeue calls
Space: O(n)
"""
from typing import Any


class Queue:
    def __init__(self) -> None:
        self.s1: list[Any] = []
        self.s2: list[Any] = []

    def enqueue(self, x: Any) -> None:
        self.s1.append(x)

    def dequeue(self) -> Any:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
            if not self.s2:
                return None

        return self.s2.pop()


cases = (
    (1, [], None),
    (2, ["q.enqueue(1)", "q.dequeue()"], None),
)
for case_id, ops, want in cases:
    q = Queue()
    for op in ops:
        exec(op)
    got = q.dequeue()
    assert got == want, f"got: {got}, want: {want} ({case_id})"
