#! /usr/bin/env python3
from typing import List

"""09/09/2019

Solution:
Once clockwise distance is computed, the counter-clockwise distance can be
easily derived by the total distance minus the clockwise distance. The only
trick to pay attention to is to make sure `start` is smaller than `destination`
when doing the clockwise computation.

Clocked in at 52 ms, 80%
"""


class Solution:
    def distanceBetweenBusStops(
        self, distance: List[int], start: int, destination: int
    ) -> int:
        total = sum(distance)
        # note that to make the clockwise computation work, start must be smaller than destination
        if start > destination:
            start, destination = destination, start
        clockwise = sum(distance[start:destination])
        counter_clock = total - clockwise
        return min(clockwise, counter_clock)


sol = Solution()
distance = [1, 2, 3, 4]
start = 0
destination = 3
print(sol.distanceBetweenBusStops(distance, start, destination))
