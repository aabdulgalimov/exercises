"""
At the end of the year all employees of an IT-company go to celebrate the new year. Buses are waiting in the parking lot of the office building with n floors.

ai employees work on the i-th floor and the parking lot is located on the zero floor.
The single lift is located at the zero floor at the start.
Lift moves at the speed of 1 floor per second and boarding/disembarking is instantaneous.

Find the minimum amount of time in which the lift can take all employees to the parking lot.

Input:
    First line contains an integer k - amount of people which can fit into the lift (1 ≤ k ≤ 10^9).
    Second line contains an integer n - number of floors in the building (1 ≤ n ≤ 10^5).
    Next n lines contain an integer ai - number of employees on the i-th floor (0 ≤ ai ≤ 10^9).

Output:
    Amount of time in seconds.

Time: O(n)
Space: O(1)
"""
import io
from contextlib import redirect_stdout
from unittest.mock import patch


def solution():
    capacity = int(input())
    floor_count = int(input())
    floors = [int(input()) for _ in range(floor_count)]
    total_time = 0
    load = 0
    last_max_floor = None
    for floor in range(floor_count, 0, -1):
        head_count = floors[floor - 1]
        if head_count:
            load += head_count
            if load >= capacity:
                trip_count = load // capacity
                if last_max_floor:
                    total_time += last_max_floor * 2
                    trip_count -= 1
                total_time += trip_count * floor * 2
                load = load % capacity
                last_max_floor = floor if load else None
            elif not last_max_floor:
                last_max_floor = floor
    if last_max_floor:
        total_time += last_max_floor * 2
    print(total_time)


cases = (
    (["2", "3", "3", "0", "1"], "8"),
    (["2", "3", "3", "0", "1", "0"], "8"),
    (["2", "3", "3", "0", "2"], "10"),
    (["3", "1", "0"], "0"),
)
for data, want in cases:
    with patch("builtins.input", side_effect=data):
        with redirect_stdout(io.StringIO()) as f:
            solution()
            got = f.getvalue()[:-1]
            assert got == want, f"got: {got}, want: {want} ({data})"
