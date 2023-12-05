"""
Write a function that evaluates a sequence of round/square/curly brackets and check whether that sequence is correct.
If sequence A is correct, then sequences (A), [A], {A} are also correct. If sequences A and B are correct, then sequence AB is also correct. Empty sequence is correct.

Input:
    A string of brackets no longer than 10^5.

Output:
    "yes" or "no".

Time: O(n)
Space: O(n)
"""
import io
from contextlib import redirect_stdout
from unittest.mock import patch


def solution():
    s = input()
    stack = []
    for c in s:
        if c == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                print("no")
                break
        elif c == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                print("no")
                break
        elif c == "}":
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                print("no")
                break
        else:
            stack.append(c)
    else:
        print("no" if stack else "yes")


cases = (
    (["()[]"], "yes"),
    (["([)]"], "no"),
    (["("], "no"),
    (["({[]})[]"], "yes"),
    (["{({[]})[]}"], "yes"),
)
for data, want in cases:
    with patch("builtins.input", side_effect=data):
        with redirect_stdout(io.StringIO()) as f:
            solution()
            got = f.getvalue()[:-1]
            assert got == want, f"got: {got}, want: {want} ({data})"
