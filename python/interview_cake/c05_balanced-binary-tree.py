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


tree1 = BinaryTreeNode(1)
tree1.insert_left(2)

tree2 = BinaryTreeNode(2)
tree2.insert_left(2)
tree2.insert_right(3)

tree3 = BinaryTreeNode(3)
tree3.insert_left(2)
tree3.left.insert_left(3)

tree4 = BinaryTreeNode(4)
tree4.insert_left(2)
tree4.insert_right(3)
tree4.left.insert_left(4)

tree5 = BinaryTreeNode(5)
tree5.insert_left(2)
tree5.insert_right(3)
tree5.left.insert_left(4)
tree5.left.left.insert_left(5)

cases = (
    (tree1, True),
    (tree2, True),
    (tree3, True),
    (tree4, True),
    (tree5, False),
)
for tree, want in cases:
    got = is_tree_superbalanced(tree)
    assert got == want, f"got: {got}, want: {want} ({tree.value})"
