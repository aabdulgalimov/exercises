"""
You have a function rand7() that generates a random integer from 1 to 7. Use it to write a function rand5() that generates a random integer from 1 to 5.

rand7() returns each integer with equal probability. rand5() must also return each integer with equal probability.

Time: O(inf)
Space: O(1)
"""

from random import randint


def rand7():
    return randint(1, 7)


def rand5():
    while True:
        num = rand7()
        if num <= 5:
            return num


rand5()
