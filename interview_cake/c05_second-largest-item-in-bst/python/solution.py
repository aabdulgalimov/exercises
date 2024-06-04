"""
Write a method to find the 2nd largest element in a binary search tree.

Time: O(h)
Space: O(1)
"""


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


def get_largest_item(root: BinaryTreeNode) -> int:
    node = root
    while node.right:
        node = node.right
    return node.value


def get_second_largest_item(root: BinaryTreeNode) -> int:
    if not (root.left or root.right):
        raise Exception("tree must have at least 2 nodes")
    node = root
    while True:
        if node.right:
            if not (node.right.left or node.right.right):
                return node.value
            else:
                node = node.right
        else:
            node = node.left
            while node.right:
                node = node.right
            return node.value


cases = (
    (3, ["root.insert_left(1)"], 1),
    (3, ["root.insert_right(5)"], 3),
    (3, ["root.insert_right(5)", "root.right.insert_right(7)"], 5),
    (3, ["root.insert_left(1)", "root.insert_right(5)"], 3),
    (3, ["root.insert_left(2)", "root.left.insert_left(1)"], 2),
    (5, ["root.insert_left(3)", "root.left.insert_right(4)"], 4),
)
for root_value, tree, want in cases:
    root = BinaryTreeNode(root_value)
    for cmd in tree:
        exec(cmd)
    got = get_second_largest_item(root)
    assert got == want, f"got: {got}, want: {want} ({root_value}, {tree})"
