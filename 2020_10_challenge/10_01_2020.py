# from pudb import set_trace; set_trace()
from typing import List
from bisect import bisect_right
from collections import deque


class RecentCounter:
    """92% ranking. Easy question"""

    def __init__(self):
        self.times = []

    def ping(self, t: int) -> int:
        self.times.append(t)
        left = bisect_right(self.times, t - 3000)
        if self.times[left - 1] == t - 3000:
            left = left - 1
        return len(self.times) - left


class RecentCounter2:
    """Improve on memory usage.

    At the end, it improves memory usage just a little bit, from 5% to ~20%
    ranking. No apparent degradation on performance.
    """

    def __init__(self):
        self.times = deque()

    def ping(self, t: int) -> int:
        self.times.append(t)
        left = bisect_right(self.times, t - 3000)
        if self.times[left - 1] == t - 3000:
            left = left - 1
        res = len(self.times) - left
        # clean up unused times
        while left:
            self.times.popleft()
            left -= 1
        return res

