"""
Write a function to check that a binary tree is a valid binary search tree.

Time: O(n)
Space: O(n)
"""


class BinaryTreeNode(object):
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


def is_valid_bst(root: BinaryTreeNode) -> bool:
    stack = [(root, None, None)]
    while stack:
        node, min_value, max_value = stack.pop()
        if (min_value and node.value < min_value) or (
            max_value and node.value > max_value
        ):
            return False
        if node.left:
            stack.append((node.left, min_value, node.value))
        if node.right:
            stack.append((node.right, node.value, max_value))
    return True


cases = (
    (3, ["root.insert_left(1)"], True),
    (3, ["root.insert_left(5)"], False),
    (3, ["root.insert_right(5)"], True),
    (3, ["root.insert_right(1)"], False),
    (3, ["root.insert_left(1)", "root.insert_right(5)"], True),
    (3, ["root.insert_left(5)", "root.insert_right(5)"], False),
    (3, ["root.insert_left(1)", "root.insert_right(1)"], False),
    (3, ["root.insert_left(2)", "root.left.insert_left(1)"], True),
    (
        3,
        [
            "root.insert_left(2)",
            "root.left.insert_left(1)",
            "root.left.insert_right(5)",
        ],
        False,
    ),
)
for root_value, tree, want in cases:
    root = BinaryTreeNode(root_value)
    for cmd in tree:
        exec(cmd)
    got = is_valid_bst(root)
    assert got == want, f"got: {got}, want: {want} ({root_value}, {tree})"
