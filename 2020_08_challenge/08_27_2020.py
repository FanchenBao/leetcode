# from pudb import set_trace; set_trace()
from typing import List
import heapq


class Solution1:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        """Sort the starts and ends separately and then check one by one"""
        size = len(intervals)
        starts = sorted([(s, i) for i, (s, e) in enumerate(intervals)], key=lambda x: x[0])
        ends = sorted([(e, i) for i, (s, e) in enumerate(intervals)], key=lambda x: x[0])
        res = [-1] * size
        si, ei = 0, 0
        while si < size and ei < size:
            if starts[si][0] < ends[ei][0]:
                si += 1
            else:
                res[ends[ei][1]] = starts[si][1]
                ei += 1
        return res


class Solution2:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        """Avoid sorting. Use heapq"""
        starts = [(s, i) for i, (s, e) in enumerate(intervals)]
        ends = [(e, i) for i, (s, e) in enumerate(intervals)]
        heapq.heapify(starts)
        heapq.heapify(ends)
        res = [-1] * len(intervals)
        while starts and ends:
            start = starts[0]
            end = ends[0]
            if end[0] <= start[0]:
                res[end[1]] = start[1]
                heapq.heappop(ends)
            else:
                heapq.heappop(starts)
        return res


sol = Solution2()

tests = [
    ([[1, 2]], [-1]),
    ([[3, 4], [2, 3], [1, 2]], [-1, 0, 1]),
    ([[1, 4], [2, 3], [3, 4]], [-1, 2, -1]),
]
for i, (test, ans) in enumerate(tests):
    res = sol.findRightInterval(test)
    if res == ans:
        print(f'Test {i}: PASS!')
    else:
        print(f'Test {i}: FAIL! Ans: {ans}, Res: {res}')