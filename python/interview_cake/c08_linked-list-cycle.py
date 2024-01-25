"""
Check whether a singly-linked list contains a cycle, given the first node of the list.

Time: O(n)
Space: O(1)
"""


class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def contains_cycle(node: LinkedListNode) -> bool:
    p1, p2 = node, node
    while p1 is not None and p1.next is not None:
        p1 = p1.next.next
        p2 = p2.next
        if p1 is p2:
            return True
    return False


cases = (
    (
        1,
        (
            "n.next = LinkedListNode(2); n = n.next",
            "n.next = LinkedListNode(3); n = n.next",
            "n.next = LinkedListNode(4);",
        ),
        False,
    ),
    (
        2,
        (
            "n.next = LinkedListNode(2); n = n.next",
            "n.next = LinkedListNode(3); p = n; n = n.next",
            "n.next = LinkedListNode(4); n = n.next",
            "n.next = p",
        ),
        True,
    ),
)
for case_id, ops, want in cases:
    first_node = LinkedListNode(1)
    n = first_node
    for op in ops:
        exec(op)
    got = contains_cycle(first_node)
    assert got == want, f"got: {got}, want: {want} ({case_id})"
