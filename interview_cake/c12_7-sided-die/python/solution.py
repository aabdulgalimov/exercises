"""
You have a function rand5() that generates a random integer from 1 to 5. Use it to write a function rand7() that generates a random integer from 1 to 7.
rand5() returns each integer with equal probability. rand7() must also return each integer with equal probability.

Time: O(inf)
Space: O(1)
"""

from random import randint


def rand5():
    return randint(1, 5)


def rand7():
    while True:
        n = (rand5() - 1) * 5 + rand5()
        if n > 21:
            continue
        return n % 7 + 1


rand7()
