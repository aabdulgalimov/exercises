"""
You wrote a trendy new messaging app, MeshMessage, to get around flaky cell phone coverage.

Instead of routing texts through cell towers, your app sends messages via the phones of nearby users, passing each message along from one phone to the next until it reaches the intended recipient.

Some friends have been using your service, and they're complaining that it takes a long time for messages to get delivered.
After some preliminary debugging, you suspect messages might not be taking the most direct route from the sender to the recipient.

Given information about active users on the network, find the shortest route for a message from one user (the sender) to another (the recipient).
Return a list of users that make up this route.

Your network information takes the form of a dictionary mapping username strings to a list of other users nearby.

Time: O(N+M)
Space: O(N)
"""
import collections


def find_shortest_route(
    network: dict[str, list[str]],
    sender: str,
    recipient: str,
) -> list[str] | None:
    queue = collections.deque()
    queue.append(sender)
    visited: dict[str, str | None] = {sender: None}  # {node: prev_node, ...}
    while queue:
        node = queue.popleft()
        if node == recipient:
            path: list[str] = []
            n = node
            while n:
                path.append(n)
                n = visited[n]
            path.reverse()
            return path
        for n in network[node]:
            if n not in visited:
                queue.append(n)
                visited[n] = node
    return None


cases = (
    (
        {
            "Jayden": ["Amelia", "Noam"],
            "Amelia": ["Jayden", "Adam", "Miguel"],
            "Adam": ["Amelia", "Miguel"],
            "Miguel": ["Amelia", "Adam", "Liam"],
            "Noam": ["Jayden"],
        },
        "Jayden",
        "Adam",
        ["Jayden", "Amelia", "Adam"],
    ),
    (
        {
            "Adam": ["Lucas"],
            "Lucas": ["Adam"],
            "Sofia": ["Ren"],
            "Ren": ["Sofia"],
        },
        "Adam",
        "Ren",
        None,
    ),
    (
        {
            "Adam": ["Sofia", "Lucas"],
            "Lucas": ["Adam"],
            "Sofia": ["Adam"],
        },
        "Adam",
        "Adam",
        ["Adam"],
    ),
)
for network, sender, recipient, want in cases:
    got = find_shortest_route(network, sender, recipient)
    assert got == want, f"got: {got}, want: {want}"
