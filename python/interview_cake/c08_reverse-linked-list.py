"""
Write a function for reversing a linked list in-place given a head node of the linked list. It should return the new head node.

Time: O(n)
Space: O(1)
"""


class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_ll(node: LinkedListNode) -> LinkedListNode:
    last_node = node
    node = node.next
    last_node.next = None
    while node:
        next_node = node.next
        node.next = last_node
        last_node = node
        node = next_node
    return last_node


cases = (
    (
        1,
        (
            "head_node.next = LinkedListNode(2)",
            "head_node.next.next = LinkedListNode(3)",
        ),
        3,
    ),
    (
        2,
        tuple(),
        1,
    ),
)
for case, ops, want in cases:
    head_node = LinkedListNode(1)
    for op in ops:
        exec(op)
    got = reverse_ll(head_node)
    assert got.value == want, f"got: {got.value}, want: {want} ({case})"
