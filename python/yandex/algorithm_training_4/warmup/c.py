"""
The Moscow mayor's office thoroughly prepared for the celebration of the city's millennium in 2147 and built an endless paved area under the capital to replace all existing roads in the city.
In memory of ring and radial roads, it was allowed to move around the site in only two ways:
1) Towards or away from the origin point (it is allowed to move from the origin point in any direction).
2) Along a circle with a center at the origin point. Moving along such a circle is allowed in any direction (clockwise or counterclockwise).

Write a function which will find a shortest path from point A to point B. Movement direction can be changed as much as needed, but the above rules must be observed.

Input:
    4 integers xA, yA, xB, yB with modulus not exceeding 10^6 (separated by a space).

Output:
    Distance for the shortest path.

Time: O(1)
Space: O(1)
"""
import math
import io
from contextlib import redirect_stdout
from unittest.mock import patch


def solution():
    x1, y1, x2, y2 = (int(x) for x in input().split())
    r1 = math.sqrt(x1**2 + y1**2)
    r2 = math.sqrt(x2**2 + y2**2)
    if r1 and r2:
        angle1 = math.atan2(y1, x1)
        if angle1 < 0:
            angle1 += 2 * math.pi
        angle2 = math.atan2(y2, x2)
        if angle2 < 0:
            angle2 += 2 * math.pi
        angle = abs(angle1 - angle2)
        if angle > math.pi:
            angle = 2 * math.pi - angle
        arc_length = angle * min(r1, r2)
        distance = min(r1 + r2, abs(r1 - r2) + arc_length)
    else:
        distance = r1 or r2
    print(distance)


cases = (
    ("0 5 4 3", 4.636476),
    ("0 5 4 -3", 10.0),
    ("1 1 -1 -1", 2.828427),
    ("0 5 0 3", 2.0),
    ("0 0 1 1", 1.414214),
    ("0 0 0 0", 0.0),
)
for data, want in cases:
    with patch("builtins.input", side_effect=[data]):
        with redirect_stdout(io.StringIO()) as f:
            solution()
            got = f.getvalue()[:-1]
            got = round(float(got), 6)
            assert got == want, f"got: {got}, want: {want} ({data})"
