# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_right


class Solution1:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """LeetCode 57

        Two rounds of binary search for lo and hi in newInterval.

        However, the implementation is quite complicated.
        O(N + logN), 69 ms
        """
        intervals = [[-2, -1]] + intervals
        i = bisect_right(intervals, newInterval[0], key=lambda tup: tup[0])
        if intervals[i - 1][0] <= newInterval[0] <= intervals[i - 1][1]:
            j = bisect_right(intervals, newInterval[1], key=lambda tup: tup[0])
            if intervals[j - 1][0] <= newInterval[1] <= intervals[j - 1][1]:
                return intervals[1:i - 1] + [[intervals[i - 1][0], intervals[j - 1][1]]] + intervals[j:]
            else:
                return intervals[1:i - 1] + [[intervals[i - 1][0], newInterval[1]]] + intervals[j:]
        else:
            j = bisect_right(intervals, newInterval[1], key=lambda tup: tup[0])
            if intervals[j - 1][0] <= newInterval[1] <= intervals[j - 1][1]:
                return intervals[1:i] + [[newInterval[0], intervals[j - 1][1]]] + intervals[j:]
            else:
                return intervals[1:i] + [[newInterval[0], newInterval[1]]] + intervals[j:]


class Solution2:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """Standard solution from 2020-09-13

        88 ms, faster than 69.53% 
        """
        ns, ne = newInterval
        left = [inter for inter in intervals if inter[1] < ns]
        right = [inter for inter in intervals if inter[0] > ne]
        if left + right != intervals:  # we do have overlaps
            ns = min(ns, intervals[len(left)][0])
            ne = max(ne, intervals[-len(right) - 1][1])
        return left + [[ns, ne]] + right


class Solution3:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """Better binary search

        O(N + logN), 77 ms, faster than 95.87% 
        """
        ns, ne = newInterval
        i = bisect_right(intervals, ns, key=lambda tup: tup[0])
        # make sure intervals[i] is the overlapping interval with ns
        if i > 0 and intervals[i - 1][1] >= ns:
            i -= 1
        # intervals[j] is the first non-overlapping interval with ne
        j = bisect_right(intervals, ne, key=lambda tup: tup[0])
        if i != j:  # we do have overlaps
            ns = min(ns, intervals[i][0])
            ne = max(ne, intervals[j - 1][1])
        return intervals[:i] + [[ns, ne]] + intervals[j:]

        

sol = Solution3()
tests = [
    ([[1,3],[6,9]], [2,5], [[1,5],[6,9]]),
    ([[2,3],[6,9]], [0,1], [[0,1],[2,3],[6,9]]),
    ([[2,3],[6,9]], [0,2], [[0,3],[6,9]]),
    ([[2,3],[6,9]], [0,4], [[0,4],[6,9]]),
    ([[2,3],[6,9]], [3,6], [[2,9]]),
    ([[2,3],[6,9]], [4,7], [[2,3],[4,9]]),
    ([[2,3],[6,9]], [0,10], [[0,10]]),
    ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8], [[1,2],[3,10],[12,16]]),
    ([[1,5]],[6,8],[[1,5],[6,8]]),
]

for i, (intervals, newInterval, ans) in enumerate(tests):
    res = sol.insert(intervals, newInterval)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
