"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string.

Constraints:
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters

Time: O(n*m)
Space: O(1)
"""


def longest_common_prefix(strs: list[str]) -> str:
    prefix_length = 0
    for i in range(len(strs[0])):
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                break
        else:
            prefix_length += 1
            continue
        break
    return strs[0][:prefix_length]


cases = (
    (["flower", "flow", "flight"], "fl"),
    (["dog", "racecar", "car"], ""),
    (["one"], "one"),
    (["one", "object"], "o"),
)
for strs, want in cases:
    got = longest_common_prefix(strs)
    assert got == want, f"got: {got}, want: {want} ({strs})"
