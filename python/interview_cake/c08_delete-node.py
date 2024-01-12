"""
Delete a node from a singly-linked list, given only a variable pointing to that node.

Time: O(1)
Space: O(1)
"""


class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def delete_node(n: LinkedListNode):
    next_node = n.next
    if next_node:
        n.value = next_node.value
        n.next = next_node.next
    else:
        raise Exception("can't delete the last node")


a = LinkedListNode(1)
b = LinkedListNode(2)
a.next = b
delete_node(a)
assert a.value == 2
