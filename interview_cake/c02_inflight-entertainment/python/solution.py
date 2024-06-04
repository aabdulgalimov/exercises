"""
You've built an inflight entertainment system with on-demand movie streaming.

Users on longer flights like to start a second movie right when their first one ends, but they complain that the plane usually lands before they can see the ending. So you're building a feature for choosing two movies whose total runtimes will equal the exact flight length.

Write a function that takes an integer flight_length (in minutes) and a list of integers movie_lengths (in minutes) and returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length.

Time: O(n)
Space: O(n)
"""


def can_watch_two_movies(flight: int, movies: list[int]) -> bool:
    s = set()
    for movie in movies:
        if flight - movie in s:
            return True
        s.add(movie)
    return False


cases = (
    (3, [1, 2, 3], True),
    (6, [1, 2, 3], False),
    (2, [1], False),
)
for flight, movies, want in cases:
    got = can_watch_two_movies(flight, movies)
    assert got == want, f"got: {got}, want: {want} ({flight} {movies})"
