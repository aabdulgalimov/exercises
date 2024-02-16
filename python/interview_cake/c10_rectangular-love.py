"""
Write a function to find the rectangular intersection of two given rectangles.
Each side of the given rectangles is parallel with either the X-axis or the Y-axis.

Rectangle is represented by a dictionary:
    rectangle = {
        'x': 1, 'y': 1,  # coordinates of bottom-left corner
        'w': 6, 'h': 3   # width and height
    }

Time: O(1)
Space: O(1)
"""


def find_intersection(r1, r2):
    x = max(r1["x"], r2["x"])
    y = max(r1["y"], r2["y"])
    w = min(r1["x"] + r1["w"], r2["x"] + r2["w"]) - x
    h = min(r1["y"] + r1["h"], r2["y"] + r2["h"]) - y
    if w > 0 and h > 0:
        return {"x": x, "y": y, "w": w, "h": h}


cases = (
    (
        {"x": 1, "y": 1, "w": 6, "h": 3},
        {"x": 2, "y": 2, "w": 6, "h": 3},
        {"x": 2, "y": 2, "w": 5, "h": 2},
    ),
    (
        {"x": 1, "y": 1, "w": 6, "h": 3},
        {"x": 7, "y": 1, "w": 6, "h": 3},
        None,
    ),
    (
        {"x": 1, "y": 1, "w": 6, "h": 3},
        {"x": -1, "y": -1, "w": 6, "h": 3},
        {"x": 1, "y": 1, "w": 4, "h": 1},
    ),
)
for r1, r2, want in cases:
    got = find_intersection(r1, r2)
    assert got == want, f"got: {got}, want: {want} ({r1} {r2})"
