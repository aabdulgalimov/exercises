"""
A cake shop has two registers: one for take-out orders, and the other for the other folks eating inside the cafe. All the customer orders get combined into one list for the kitchen, where they should be handled first-come, first-served.

Recently, some customers have been complaining that people who placed orders after them are getting their food first.

To investigate their claims, the following lists were recorded:
    - The take-out orders as they were entered into the system and given to the kitchen. (take_out_orders)
    - The dine-in orders as they were entered into the system and given to the kitchen. (dine_in_orders)
    - Each customer order (from either register) as it was finished by the kitchen. (served_orders)

Given all three lists, write a function to check that the service is first-come, first-served. All food should come out in the same order customers requested it.

Each customer order as a unique integer.

Time: O(n)
Space: O(1)
"""


def check_orders(take_out: list[int], dine_in: list[int], served: list[int]) -> bool:
    p_out, p_in = 0, 0
    for order in served:
        if p_out < len(take_out) and order == take_out[p_out]:
            p_out += 1
        elif p_in < len(dine_in) and order == dine_in[p_in]:
            p_in += 1
        else:
            return False
    if p_out != len(take_out) or p_in != len(dine_in):
        return False
    return True


cases = (
    ([1, 3, 5], [2, 4, 6], [1, 2, 4, 6, 5, 3], False),
    ([1, 3, 5], [2, 4, 6], [1, 2, 3, 5, 4, 6], True),
    ([], [1, 2, 3], [1, 2, 3], True),
    ([1, 2], [3], [3, 2, 1], False),
    ([1, 2], [3, 4], [1, 2, 3], False),
    ([1, 2, 1], [2, 1], [], False),
)
for take_out, dine_in, served, want in cases:
    result = check_orders(take_out, dine_in, served)
    if result != want:
        print(take_out, dine_in, served)
        print(f"got: {result}, want: {want}")
        break
