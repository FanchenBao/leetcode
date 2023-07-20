# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_right


class Solution1:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """LeetCode 435

        DP with binary search. Apparently, this is not the best solution,
        because its run time is horrifyingly long.

        O(NlogN), 1867 ms, faster than 5.02% 
        """
        intervals.sort(key=lambda tup: (tup[1], tup[0]))
        pmax = [1]
        for i in range(1, len(intervals)):
            idx = bisect_right(intervals, intervals[i][0], key=lambda tup: tup[1])
            cur = 1
            if idx > 0:
                cur += pmax[idx - 1]
            pmax.append(max(pmax[-1], cur))
        return len(intervals) - pmax[-1]


class Solution2:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """Very similar solution as a few days ago. Here we use dp(idx, pre_end) to
        indicate the longest non-overlapping intervals in the range [idx:] with
        the previous interval's end as pre_end. This seems to be a 2D DP, but the
        function of pre is just to indicate whether the current interval can
        be taken. It does not count as the actual part of the DP. Thus, the DP
        is only 1D.

        O(NlogN + N), but it TLE. I think this DP would work three years ago,
        because there were only 18 test cases. Now the test cases have blown up
        to 58, this solution only passes 55 out of the 58.
        """
        intervals.sort()
        N = len(intervals)
        memo = [0] * N

        def dp(idx: int, pre_end: int) -> int:
            if idx == N:
                return 0
            if intervals[idx][0] < pre_end:  # cannot take intervals[idx]
                return dp(idx + 1, pre_end)
            if memo[idx] == 0:  # we have not checked intervals[idx] yet
                memo[idx] = max(
                    1 + dp(idx + 1, intervals[idx][1]),
                    dp(idx + 1, pre_end),
                )
            return memo[idx]

        return N - dp(0, -math.inf)


class Solution3:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """Greedy. Sort intervals based on end. The longest non-overlapping
        intervals must include those with the smallest end, because that provides
        the best opportunity to extend the intervals.

        This is a simplified version of Solution1. Greedy makes sense, because
        in solution1, we binary search for a previous position with end smaller
        or equal to the start of the current interval. However, since we use
        prefix max, as long as the previous position is not the end of prefix
        max, we always run the risk of obtaining a smaller value than the end
        of prefix max. If that is the case, then the current max will never be
        bigger than the end of prefix max. In other words, the only way to
        create bigger sequence of non-overlapping intervals is to use the end of
        prefix max, which means to include intervals with the smallest end.

        1465 ms, faster than 40.44% 
        """
        intervals.sort(key=lambda tup: (tup[1], tup[0]))
        maxlen = 0
        pre_end = -math.inf
        for s, e in intervals:
            if s >= pre_end:
                maxlen += 1
                pre_end = e
        return len(intervals) - maxlen


        
sol = Solution3()
tests = [
    ([[1,2],[2,3],[3,4],[1,3]], 1),
    ([[1,2],[1,2],[1,2]], 2),
    ([[1,2],[2,3]], 0),
]

for i, (intervals, ans) in enumerate(tests):
    res = sol.eraseOverlapIntervals(intervals)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
