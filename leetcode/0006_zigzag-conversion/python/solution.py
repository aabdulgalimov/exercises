"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows.

Constraints:
    1 <= s.length <= 1000
    s consists of English letters (lower-case and upper-case), ',' and '.'.
    1 <= numRows <= 1000

Time: O(n)
Space: O(1)
"""


def convert(s: str, num_rows: int) -> str:
    if num_rows == 1 or num_rows >= len(s):
        return s

    result: list[str] = []
    cycle = num_rows * 2 - 2

    # first row
    result.extend(s[i] for i in range(0, len(s), cycle))

    # inner rows
    for i in range(1, num_rows - 1):
        for j in range(i, len(s), cycle):
            result.append(s[j])
            j2 = j + cycle - i * 2
            if j2 < len(s):
                result.append(s[j2])

    # last row
    result.extend(s[i] for i in range(num_rows - 1, len(s), cycle))

    return "".join(result)


cases = (
    ("A", 1, "A"),
    ("A", 3, "A"),
    ("ABC", 1, "ABC"),
    ("ABC", 3, "ABC"),
    ("ABC", 2, "ACB"),
    # P   A   H   N | 0,4,8,12
    # A P L S I I G | 1,3,5,7,9,11,13
    # Y   I   R     | 2,6,10
    ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
    # P     I     N | 0,6,12
    # A   L S   I G | 1,5,7,11,13
    # Y A   H R     | 2,4,8,10
    # P     I       | 3,9
    ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
    # P       H   | 0,8
    # A     S I   | 1,7,9
    # Y   I   R   | 2,6,10
    # P L     I G | 3,5,11,13
    # A       N   | 4,12
    ("PAYPALISHIRING", 5, "PHASIYIRPLIGAN"),
    # P           N           I | 0,12,24
    # A         I G         H R | 1,11,13,23,25
    # Y       R   .       S   I | 2,10,14,22,26
    # P     I     P     I     N | 3,9,15,21,27
    # A   H       A   L       G | 4,8,16,20,28
    # L S         Y A           | 5,7,17,19
    # I           P             | 6,18
    ("PAYPALISHIRING.PAYPALISHIRING", 7, "PNIAIGHRYR.SIPIPINAHALGLSYAIP"),
)
for s, rows, want in cases:
    got = convert(s, rows)
    assert got == want, f"got: {got}, want: {want} ({s} {rows})"
