"""
Write a function that takes an integer k and the head node of a singly-linked list, and returns the kth to last node in the list.

Time: O(n)
Space: O(1)
"""


class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def find_node(k: int, node: LinkedListNode) -> LinkedListNode:
    kth_node = node

    while k > 0:
        if not node:
            raise Exception(f"node not found")
        node = node.next
        k -= 1

    while node:
        node = node.next
        kth_node = kth_node.next

    return kth_node


node = LinkedListNode(1)
node.next = LinkedListNode(2)
node.next.next = LinkedListNode(3)
kth_node = find_node(3, node)
assert kth_node.value == 1
