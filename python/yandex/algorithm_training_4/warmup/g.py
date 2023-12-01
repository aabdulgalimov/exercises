"""
Rabbits are curious. They love to study geometry by runnig around garden beds. Our rabbit is just like that. Today he decided to study a new figure - a square.
The rabbit is running around a field of N x M cells. Some of them are sown with carrots, some are not.

Help the rabbit to find a side length of the largest square fully filled with carrots.

Input:
    First line contains field dimensions - two integers N and M (1 <= N, M <= 1000).
    Next N lines contain M integers separated by a space which which represent the cell state (1 if carrot is present, 0 otherwise).

Output:
    Square side length.

Time: O(n^m)
Space: O(n^m)
"""
import io
from contextlib import redirect_stdout
from unittest.mock import patch


def solution():
    n, m = (int(x) for x in input().split())
    field = [[int(x) for x in input().split()] for _ in range(n)]
    max_side = max(field[0])
    for i in range(1, n):
        for j in range(1, m):
            if field[i][j]:
                side = 1 + min(field[i][j - 1], field[i - 1][j - 1], field[i - 1][j])
                field[i][j] = side
                if side > max_side:
                    max_side = side
    print(max_side)


cases = (
    (
        [
            "4 5",
            "0 0 0 1 0",
            "0 1 1 1 0",
            "0 0 1 1 0",
            "1 0 1 0 0",
        ],
        "2",
    ),
    (
        [
            "3 3",
            "1 1 1",
            "1 1 1",
            "1 1 1",
        ],
        "3",
    ),
    (
        [
            "3 3",
            "0 0 0",
            "0 0 0",
            "0 0 0",
        ],
        "0",
    ),
    (
        [
            "3 3",
            "0 0 0",
            "0 1 0",
            "0 0 0",
        ],
        "1",
    ),
)
for data, want in cases:
    with patch("builtins.input", side_effect=data):
        with redirect_stdout(io.StringIO()) as f:
            solution()
            got = f.getvalue()[:-1]
            assert got == want, f"got: {got}, want: {want} ({data})"
