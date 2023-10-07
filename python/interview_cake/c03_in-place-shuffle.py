"""
Write a function for doing an in-place shuffle of a list.

The shuffle must be "uniform", meaning each item in the original list must have the same probability of ending up in each spot in the final list.
Assume that you have a function get_random(floor, ceiling) for getting a random integer that is >= floor and <= ceiling.

Time: O(n)
Space: O(1)
Fisher-Yates shuffle
"""
from random import randrange


def shuffle(nums: list[int]):
    for i in range(len(nums) - 1):
        r = randrange(i, len(nums))
        if r != i:
            nums[i], nums[r] = nums[r], nums[i]


nums = [1, 2, 3, 4, 5]
shuffle(nums)
print(nums)
