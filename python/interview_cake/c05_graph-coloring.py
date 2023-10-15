"""
Given an undirected graph with maximum degree D, find a graph coloring using at most D+1 colors.

Graphs are represented by a list of N node objects, each with a label, a set of neighbors, and a color.

Time: O(N+M)
Space: O(D)
"""


class GraphNode:
    def __init__(self, label: str):
        self.label: str = label
        self.neighbors: set[GraphNode] = set()
        self.color: str | None = None


def color_graph(graph: list[GraphNode], colors: list[str]):
    for node in graph:
        if node.label in node.neighbors:
            raise Exception(f"node {node.label} has a loop edge")
        if len(node.neighbors) >= len(colors):
            raise Exception(f"node {node.label} has too many neighbors")
        taken_colors = set(n.color for n in node.neighbors if n.color)
        for color in colors:
            if color not in taken_colors:
                node.color = color
                break


cases = (
    # a - b
    #  \ /
    #   c
    (
        [
            "a = GraphNode('a')",
            "b = GraphNode('b')",
            "c = GraphNode('c')",
            "a.neighbors.add(b)",
            "b.neighbors.add(a)",
            "b.neighbors.add(c)",
            "c.neighbors.add(b)",
            "c.neighbors.add(a)",
            "graph = [a, b, c]",
        ],
        ["red", "black", "green"],
        ["red", "black", "green"],
    ),
    # a - b
    #  \ /
    #   c - d - f
    (
        [
            "a = GraphNode('a')",
            "b = GraphNode('b')",
            "c = GraphNode('c')",
            "d = GraphNode('d')",
            "f = GraphNode('f')",
            "a.neighbors.add(b)",
            "b.neighbors.add(a)",
            "b.neighbors.add(c)",
            "c.neighbors.add(b)",
            "c.neighbors.add(a)",
            "c.neighbors.add(d)",
            "d.neighbors.add(c)",
            "d.neighbors.add(f)",
            "f.neighbors.add(d)",
            "graph = [a, b, c, d, f]",
        ],
        ["red", "black", "green", "blue"],
        ["red", "black", "green", "red", "black"],
    ),
)

for graph_init, colors, want in cases:
    graph = []
    for cmd in graph_init:
        exec(cmd)
    color_graph(graph, colors)
    got = [node.color for node in graph]
    assert got == want, f"got: {got}, want: {want} ({graph_init})"
