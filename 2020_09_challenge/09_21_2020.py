# from pudb import set_trace; set_trace()
from typing import List
import heapq


class Solution1:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """Have to use priority queue for this solution. 
        Passed OJ at 58 percentile.
        """
        unpicked, ongoing = [], []
        for c, s, e in trips:
            heapq.heappush(unpicked, (s, e, c))
        tick = unpicked[0][0]
        while unpicked:
            while ongoing and ongoing[0][0] == tick:
                capacity += heapq.heappop(ongoing)[1]
            while unpicked and unpicked[0][0] == tick:
                s, e, c = heapq.heappop(unpicked)
                capacity -= c
                if capacity < 0:
                    return False
                heapq.heappush(ongoing, (e, c))
            tick += 1
        return True


class Solution2:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """Avoid using priority queue. Use bucket sort instead.

        If the range for the max end point is not given, use regular sort
        instead.

        The genius move in this solution is to create a net change array of
        capacity at each point in the trip. This avoids the use of two priority
        queue to keep track of the current trip status.
        """
        sorted_trips = [0] * 1001  # max end point is 1000
        for c, s, e in trips:
            sorted_trips[s] -= c  # record the net change in passenages at each point
            sorted_trips[e] += c
        for c in sorted_trips:
            capacity += c
            if capacity < 0:
                return False
        return True


sol = Solution2()
tests = [
    ([[2, 1, 5], [3, 3, 7]], 4, False),
    ([[2, 1, 5], [3, 3, 7]], 5, True),
    ([[2, 1, 5], [3, 5, 7]], 3, True),
    ([[3, 2, 7], [3, 7, 9], [8, 3, 9]], 11, True),
    ([[5, 4, 7], [7, 4, 8], [4, 1, 8]], 17, True),
    ([[3, 2, 8], [4, 4, 6], [10, 8, 9]], 11, True),
]

for i, (trips, capacity, ans) in enumerate(tests):
    res = sol.carPooling(trips, capacity)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
