"""
Write a function to see if a binary tree is "superbalanced" (a new tree property we just made up).
A tree is "superbalanced" if the difference between the depths of any two leaf nodes is no greater than one.

Time: O(n)
Space: O(n)
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


def is_tree_superbalanced(root: BinaryTreeNode) -> bool:
    depths: list[int] = []
    stack = [(root, 0)]
    while stack:
        node, depth = stack.pop()
        if not (node.left or node.right):
            if depth not in depths:
                if len(depths) == 2 or (depths and abs(depths[0] - depth) > 1):
                    return False
                else:
                    depths.append(depth)
        else:
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
    return True


cases = (
    (["root.insert_left(1)"], True),
    (["root.insert_left(1)", "root.insert_right(2)"], True),
    (["root.insert_left(1)", "root.left.insert_left(2)"], True),
    (
        [
            "root.insert_left(1)",
            "root.insert_right(2)",
            "root.left.insert_left(3)",
        ],
        True,
    ),
    (
        [
            "root.insert_left(1)",
            "root.insert_right(2)",
            "root.left.insert_left(3)",
            "root.left.left.insert_left(4)",
        ],
        False,
    ),
)
for tree, want in cases:
    root = BinaryTreeNode(0)
    for cmd in tree:
        exec(cmd)
    got = is_tree_superbalanced(root)
    assert got == want, f"got: {got}, want: {want} ({tree})"
