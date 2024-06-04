"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol   Value
I        1
V        5
X        10
L        50
C        100
D        500
M        1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Constraints:
    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range [1, 3999].

Time: O(n)
Space: O(1)
"""


def roman_to_int(s: str) -> int:
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    last_n = d[s[-1]]
    result = last_n
    for i in range(len(s) - 2, -1, -1):
        n = d[s[i]]
        if n < last_n:
            result -= n
        else:
            result += n
        last_n = n
    return result


cases = (
    ("III", 3),
    ("LVIII", 58),
    ("MCMXCIV", 1994),
    ("IX", 9),
    ("XLI", 41),
)
for s, want in cases:
    got = roman_to_int(s)
    assert got == want, f"got: {got}, want: {want} ({s})"
