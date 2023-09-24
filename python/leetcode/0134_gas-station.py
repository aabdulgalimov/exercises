"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

Constraints:
    n == gas.length == cost.length
    1 <= n <= 10^5
    0 <= gas[i], cost[i] <= 10^4

Time: O(n)
Space: O(1)
"""


def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    start = 0
    tank = 0
    surplus = 0
    for i in range(len(gas)):
        if tank < 0:
            tank = 0
            start = i
        diff = gas[i] - cost[i]
        surplus += diff
        tank += diff
    return -1 if surplus < 0 else start


cases = (
    ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
    ([2, 3, 4], [3, 4, 3], -1),
)
for gas, cost, want in cases:
    got = can_complete_circuit(gas, cost)
    assert got == want, f"got: {got}, want: {want} ({gas} {cost})"
