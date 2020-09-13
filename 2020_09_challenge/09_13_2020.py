# from pudb import set_trace; set_trace()
from typing import List
from bisect import bisect_right


class Solution1:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """Probably one of my best attempt. Passed OJ with 73 ms runtime.
    
        98.94 percentile.
        """
        if not intervals:
            return [newInterval]
        ns, ne = newInterval
        int_starts = [interval[0] for interval in intervals]
        si = bisect_right(int_starts, ns)
        ei = bisect_right(int_starts, ne)
        if intervals[si - 1][0] <= ns <= intervals[si - 1][1]:  # in case si = 0
            pre, suf = intervals[:si - 1], intervals[ei:]
            if intervals[ei - 1][0] <= ne <= intervals[ei - 1][1]:  # in case ei = 0
                mid = [[intervals[si - 1][0], intervals[ei - 1][1]]]
            else:
                mid = [[intervals[si - 1][0], ne]]
        else:
            pre, suf = intervals[:si], intervals[ei:]
            if intervals[ei - 1][0] <= ne <= intervals[ei - 1][1]:  # in case ei = 0
                mid = [[ns, intervals[ei - 1][1]]]
            else:
                mid = [newInterval]
        return pre + mid + suf
            

class Solution2:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """Standard solution"""
        ns, ne = newInterval
        left = [interval for interval in intervals if interval[1] < ns]
        right = [interval for interval in intervals if interval[0] > ne]
        if left + right != intervals:
            ns = min(ns, intervals[len(left)][0])
            ne = max(ne, intervals[~len(right)][1])
        return left + [[ns, ne]] + right


sol = Solution2()
tests = [
    ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
    ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
    ([[1, 5]], [0, 3], [[0, 5]]),
    ([[1, 5]], [0, 0], [[0, 0], [1, 5]])
]

for i, (intervals, newInterval, ans) in enumerate(tests):
    res = sol.insert(intervals, newInterval)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
