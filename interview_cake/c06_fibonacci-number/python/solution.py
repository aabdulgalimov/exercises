"""
Write a function that takes an integer n and returns the nth Fibonacci number (n >= 0).

Time: O(n)
Space: O(1)
"""


def fib(n: int) -> int:
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


cases = ((0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8))
for n, want in cases:
    got = fib(n)
    assert got == want, f"got: {got}, want: {want} ({n})"
