"""
Implement the RandomizedSet class:
    RandomizedSet() Initializes the RandomizedSet object.
    bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
    bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
    int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity.

Constraints:
    -2^31 <= val <= 2^31 - 1
    At most 2 * 10^5 calls will be made to insert, remove, and getRandom.
    There will be at least one element in the data structure when getRandom is called.

Time: O(1)
Space: O(n)
"""
import random


class RandomizedSet:
    def __init__(self):
        self.rs: dict[int, int] = {}  # {value: index, ...}
        self.rs_list: list[int] = []

    def insert(self, val: int) -> bool:
        if val in self.rs:
            return False
        self.rs[val] = len(self.rs_list)
        self.rs_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.rs:
            return False
        i = self.rs.pop(val)
        last_val = self.rs_list.pop()
        if i < len(self.rs):
            self.rs_list[i] = last_val
            self.rs[last_val] = i
        return True

    def get_random(self) -> int:
        i = random.randint(0, len(self.rs) - 1)
        return self.rs_list[i]


rs = RandomizedSet()
print(
    rs.insert(3),
    rs.insert(3),
    rs.insert(1),
    rs.remove(3),
    rs.insert(0),
    rs.remove(0),
    rs.get_random(),
)
