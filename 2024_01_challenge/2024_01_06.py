# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache
from bisect import bisect_left


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        LeetCode 1235

        Not too difficult a DP problem, where DP(idx) is the max profit starting from job[idx].
        Here, job array (or comb_time array in the implementation) is a sorted array by start
        time.

        To solve DP(idx), we have two options: either not take job[idx], in which case the result
        would be DP(idx + 1), or take job[idx], in which case the result would be the profit of
        job[idx] plus DP(j) where job[j] is the earliest job whose starting time does not overlap
        that of job[idx].

        O(NlogN), 692 ms, faster than 46.73%
        """
        # comb_time = sorted((s, e, p) for s, e, p in zip(startTime, endTime, profit))
        comb_time = sorted(zip(startTime, endTime, profit))
        N = len(startTime)
        
        @lru_cache(maxsize=None)
        def dp(idx: int) -> int:
            if idx == N:
                return 0
            # option 1: not take the current job
            res = dp(idx + 1)
            # option 2: take the current job and find the earliest next job to run dp
            j = bisect_left(comb_time, comb_time[idx][1], key=lambda tup : tup[0])
            return max(res, comb_time[idx][2] + dp(j))

        return dp(0)


sol = Solution()
tests = [
    ([1,2,3,3],[3,4,5,6],[50,10,40,70], 120),
    ([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60], 150),
]

for i, (startTime, endTime, profit, ans) in enumerate(tests):
    res = sol.jobScheduling(startTime, endTime, profit)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
