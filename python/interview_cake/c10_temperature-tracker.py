"""
You decide to test if your oddly-mathematical heating company is fulfilling its All-Time Max, Min, Mean and Mode Temperature Guarantee™.

Write a class TempTracker with these methods:
    insert() - records a new temperature
    get_max() - returns the highest temp we've seen so far
    get_min() - returns the lowest temp we've seen so far
    get_mean() - returns the mean of all temps we've seen so far (float)
    get_mode() - returns a mode of all temps we've seen so far

Optimize for time in get_max(), get_min(), get_mean() and get_mode() methods.
Temperatures will all be inserted as integers (in the range of 0..110).
get_mean() should return a float, but the rest of the getter methods can return integers.
If there is more than one mode, return any of the modes.

Time: O(1)
Space: O(1)
"""


class TempTracker:
    def __init__(self) -> None:
        self.min_temp = None
        self.max_temp = None

        self.mean_temp = None
        self.temp_sum = 0
        self.temp_count = 0

        self.mode_temp = None
        self.counts = [0] * 111  # 0..110
        self.max_count = 0

    def insert(self, t: int) -> None:
        if not self.max_temp or t > self.max_temp:
            self.max_temp = t
        if not self.min_temp or t < self.min_temp:
            self.min_temp = t

        self.temp_sum += t
        self.temp_count += 1
        self.mean_temp = self.temp_sum / self.temp_count

        self.counts[t] += 1
        if self.counts[t] > self.max_count:
            self.max_count = self.counts[t]
            self.mode_temp = t

    def get_max(self) -> int:
        return self.max_temp

    def get_min(self) -> int:
        return self.min_temp

    def get_mean(self) -> float:
        return self.mean_temp

    def get_mode(self) -> int:
        return self.mode_temp


tt = TempTracker()
tt.insert(1)
tt.insert(2)
tt.insert(3)
tt.insert(3)
assert tt.get_max() == 3
assert tt.get_min() == 1
assert tt.get_mean() == 2.25
assert tt.get_mode() == 3
