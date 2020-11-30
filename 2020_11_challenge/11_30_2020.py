# from pudb import set_trace; set_trace()
from typing import List
import heapq
import itertools
import collections


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """I gave up on this.
        This is a good (but not easy to understand) article explaining the key
        concept of the solution: https://briangordon.github.io/2014/08/the-skyline-problem.html

        The key concept is to find the max height of each critical point. A
        critical point is defined as the top two corners of each building.

        We use a heap to record the max heights of all rectangle at each
        critical point. This allows us to report the max value in O(log(N)) time
        """
        # Python itertool magic, use chain.from_iterable to flatten a list of
        # list. See answer here: https://stackoverflow.com/a/13959027/9723036
        building_map = collections.defaultdict(list)
        for li, ri, hi in buildings:
            building_map[li].append([-hi, ri])
        # critical points
        cps = sorted(set(itertools.chain.from_iterable([li, ri] for li, ri, _ in buildings)))
        heap = []  # heap to keep track of current building state at each cp
        res = []
        for cp in cps:
            for bd in building_map.get(cp, []):  # always add new building on left edge
                heapq.heappush(heap, bd)
            while heap and heap[0][1] <= cp:  # pop heighest building not reachable by current cp
                heapq.heappop(heap)
            ch = -heap[0][0] if heap else 0  # critical point height
            if not res or res[-1][1] != ch:
                res.append([cp, ch])
        # print(building_map)
        # print(cps)
        # print(cp_heights)
        return res


sol = Solution()
tests = [
    ([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]], [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]),
    ([[1, 2, 1], [1, 2, 2], [1, 2, 3]], [[1, 3], [2, 0]]),
    ([[0, 5, 7], [5, 10, 7], [5, 10, 12], [10, 15, 7], [15, 20, 7], [15, 20, 12], [20, 25, 7]], [[0, 7], [5, 12], [10, 7], [15, 12], [20, 7], [25, 0]]),
    ([[2, 4, 7], [2, 4, 5], [2, 4, 6]], [[2, 7], [4, 0]]),
    ([[3, 7, 8], [3, 8, 7], [3, 9, 6], [3, 10, 5], [3, 11, 4], [3, 12, 3], [3, 13, 2], [3, 14, 1]], [[3, 8], [7, 7], [8, 6], [9, 5], [10, 4], [11, 3], [12, 2], [13, 1], [14, 0]]),
]

for i, (buildings, ans) in enumerate(tests):
    res = sol.getSkyline(buildings)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
