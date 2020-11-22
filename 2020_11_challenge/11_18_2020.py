# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """70% ranking.

        Sorting based on the end. But it seems unnecessarily complicated. I
        remember other questions based on sorting of the ends, but
        maybe this question is not.
        """
        intervals.sort(key=lambda lst: lst[1])
        res = [intervals[0]]
        for start, end in intervals[1:]:
            while res and start < res[-1][0]:
                res.pop()
            if res and start <= res[-1][1]:
                res[-1][1] = end
            else:
                res.append([start, end])
        return res


class Solution2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """Try sorting based on starts"""
        intervals.sort(key=lambda lst: lst[0])
        res = [intervals[0]]
        for start, end in intervals[1:]:
            if start > res[-1][1]:
                res.append([start, end])
            else:
                res[-1][1] = max(res[-1][1], end)
        return res


sol = Solution2()
tests = [
    ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
    ([[1, 4], [4, 5]], [[1, 5]]),
    ([[1, 4], [0, 5]], [[0, 5]]),
    ([[1, 4], [0, 4]], [[0, 4]]),
    ([[1, 3], [4, 6], [0, 18], [15, 18]], [[0, 18]]),
]

for i, (intervals, ans) in enumerate(tests):
    res = sol.merge(intervals)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
