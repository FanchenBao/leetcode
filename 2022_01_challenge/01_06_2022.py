# from pudb import set_trace; set_trace()
from typing import List
import heapq


class Solution1:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """LeetCode 1094

        We use priority queue for this. At each step, we pop out a range with
        the smallest starting point. We check it with the current range, and
        decide what the next current range should be. This means we try to
        find the overlap between the two ranges. The overlap part has the
        occupancy summed, and the left over needs to be pushed back to the
        priority queue.

        1187 ms, 5% ranking.
        """
        for tr in trips:
            tr[0], tr[1], tr[2] = tr[1], tr[2], tr[0]
        heapq.heapify(trips)
        lo, hi, occ = 0, 0, 0
        while trips:
            cur_lo, cur_hi, cur_occ = heapq.heappop(trips)
            if cur_lo >= hi:
                lo, hi, occ = cur_lo, cur_hi, cur_occ
            else:
                if hi < cur_hi:
                    heapq.heappush(trips, [hi, cur_hi, cur_occ])
                elif hi > cur_hi:
                    heapq.heappush(trips, [cur_hi, hi, occ])
                lo, hi, occ = cur_lo, min(hi, cur_hi), occ + cur_occ
            if occ > capacity:
                return False
        return True


class Solution2:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """This is the priority queue solution from Sep. 2020

        The idea is to keep two priority queues. One recording the starting
        point of each journey, and the other the end point. We tick through
        each distance. When the starting point hits the tick, we reduce
        capacity (i.e. allow people to come on); whereas when the end point
        hits the tick, we increase capacity (i.e. people get off). This is a
        very neat idea.

        O(NlogN), 136 ms, 11% ranking (there are more test cases than before).

        This solution is faster than solution1 because we only have to go
        through everything in trips. In other words, we do not have to care
        about the endings of each trip. In solution1, by the time trips are
        exhausted, we will have considered both the starting and ending point.
        """
        for tr in trips:
            tr[0], tr[1], tr[2] = tr[1], tr[2], tr[0]
        heapq.heapify(trips)
        endings = []
        dist = trips[0][0]
        while trips:
            while endings and endings[0][0] == dist:
                capacity += heapq.heappop(endings)[1]
            while trips and trips[0][0] == dist:
                lo, hi, occ = heapq.heappop(trips)
                capacity -= occ
                if capacity < 0:
                    return False
                heapq.heappush(endings, [hi, occ])
            dist += 1
        return True


class Solution3:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """Solution2 reveals that we reduce capacity at each starting point of
        the trip and increase capacity at each end point. Thus, we can create
        an array to record the net change of capacity at each appropriate
        distance.

        O(N), 64 ms, 86% ranking.
        """
        net_cap = [0] * 1001
        for occ, lo, hi in trips:
            net_cap[lo] -= occ
            net_cap[hi] += occ
        for nc in net_cap:
            capacity += nc
            if capacity < 0:
                return False
        return True


sol = Solution3()
tests = [
    ([[2,1,5],[3,3,7]], 4, False),
    ([[2,1,5],[3,3,7]], 5, True),
    ([[2,1,5],[3,5,7]], 3, True),
    ([[5,4,7],[7,4,8],[4,1,8]], 17, True),
]

for i, (trips, capacity, ans) in enumerate(tests):
    res = sol.carPooling(trips, capacity)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
