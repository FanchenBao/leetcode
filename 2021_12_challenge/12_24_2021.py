# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """LeetCode 56

        Sort intervals by starting point. Keep track of the current range.
        Each new range comes in, we compare the new lo with the current hi.
        If the new lo is larger than current hi, the current range is done. We
        save it and update it. Otherwise, we extend the current hi based on
        the max value of the current hi and the new hi.

        O(N), 88 ms, 53% ranking.
        """
        intervals.sort()
        res = []
        lo, hi = intervals[0]
        for a, b in intervals[1:]:
            if a > hi:
                res.append([lo, hi])
                lo, hi = a, b
            else:
                hi = max(hi, b)
        return res + [[lo, hi]]


sol = Solution()
tests = [
    ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
    ([[1,4],[4,5]], [[1,5]]),
]

for i, (intervals, ans) in enumerate(tests):
    res = sol.merge(intervals)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
