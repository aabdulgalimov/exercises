"""
Your company delivers breakfast via autonomous quadcopter drones. And something mysterious has happened.

Each breakfast delivery is assigned a unique ID, a positive integer.
When one of the company's 100 drones takes off with a delivery, the delivery's ID is added to a list, delivery_id_confirmations.
When the drone comes back and lands, the ID is again added to the same list.

After breakfast this morning there were only 99 drones on the tarmac.
One of the drones never made it back from a delivery.
We suspect a secret agent from Amazon placed an order and stole one of our patented drones.
To track them down, we need to find their delivery ID.

Given the list of IDs, which contains many duplicate integers and one unique integer, find the unique integer.

The IDs are not guaranteed to be sorted or sequential.
Orders aren't always fulfilled in the order they were received.

Time: O(n)
Space: O(1)
"""


def find_unique_delivery_id(log: list[int]) -> int:
    result = 0
    for delivery_id in log:
        result ^= delivery_id
    return result


cases = (
    ([1, 2, 3, 1, 2], 3),
    ([1, 2, 3, 2, 3, 1], 0),
)
for deliveries, want in cases:
    got = find_unique_delivery_id(deliveries)
    assert got == want, f"got: {got}, want: {want} ({deliveries})"
