"""
There is a vault with a limited number of types of cakes (m) and an unlimited supply of each type. Each type of cake has a weight and a value.
You brought a duffel bag that can hold limited weight (n) and you want to make off with the most valuable haul possible.

Write a function that takes a list of cake type tuples (weight, value) and a weight capacity, and returns the maximum monetary value the duffel bag can hold.
Weights and values may be any non-negative integer.

Time: O(n*m)
Space: O(n)
"""


def max_value(cakes: list[tuple[int]], capacity: int) -> int:
    for weight, value in cakes:
        if weight == 0 and value > 0:
            raise Exception("max value is infinity")

    max_values = [0] * (capacity + 1)
    for current_capacity in range(capacity + 1):
        max_value = 0
        for weight, value in cakes:
            if weight <= current_capacity:
                cake_max_value = value + max_values[current_capacity - weight]
                if cake_max_value > max_value:
                    max_value = cake_max_value
        max_values[current_capacity] = max_value
    return max_values[capacity]


cases = (
    ([(7, 160), (3, 90), (2, 15)], 20, 555),
    ([(1, 1)], 0, 0),
)
for cakes, capacity, want in cases:
    got = max_value(cakes, capacity)
    assert got == want, f"got: {got}, want: {want} ({cakes} {capacity})"
