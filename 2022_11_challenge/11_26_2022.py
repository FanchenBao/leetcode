# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache
from bisect import bisect_left


class Solution1:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """LeetCode 1235

        First sort all the jobs based on its start ttime.

        Then use dfs(i) to compute the max profit taking job i, i + 1, ..., N - 1
        After taking job i, we need to find the earliest next job to take. We
        call it job nidx. The important thing to note is that we don't have to
        check each of dfs(nidx), dfs(nidx + 1), ..., dfs(N - 1), because once
        the job gets outside the range of job nidx, it is guaranteed that its
        profit is smaller than some job before it.

        Of course, this is NOT the right way to do it.

        O(NlogN)-ish, 3085 ms, faster than 5.03% 
        """
        jobs = sorted(zip(startTime, endTime, profit))
        N = len(jobs)

        @lru_cache(maxsize=None)
        def dfs(idx: int) -> int:
            nidx = bisect_left(jobs, jobs[idx][1], key=lambda tup: tup[0])
            if nidx == N:
                return jobs[idx][2]
            res, i = 0, nidx
            while i < N and jobs[i][0] < jobs[nidx][1]:
                res = max(res, dfs(i))
                i += 1
            return res + jobs[idx][2]

        res, i = 0, 0
        while i < N and jobs[i][0] < jobs[0][1]:
            res = max(res, dfs(i))
            i += 1
        return res


class Solution2:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """This is from the solution last time on 2021-08-28.

        This is the right way to do it. Bottom up DP. We consider dp[i] as the
        max profit from job i to the end. NOTE that this does not mean we have
        to take job i. It just means the max profit from some jobs from job i
        to the end. Then, when we encounter job i, we can take job i, then we
        must find the next possible job such that dp[i] = profit[i] + dp[nidx]
        Or, we can decide not to take job i, then dp[i] = dp[i + 1]

        So dp[i] = max(profit[i] + dp[nidx], dp[i + 1])

        O(NlogN), 1694 ms, faster than 27.69%
        """
        jobs = sorted(zip(startTime, endTime, profit))
        N = len(jobs)
        dp = [0] * (N + 1)
        for i in range(N - 1, -1, -1):
            nidx = bisect_left(jobs, jobs[i][1], key=lambda tup: tup[0])
            dp[i] = max(jobs[i][2] + dp[nidx], dp[i + 1])
        return dp[0]
        

sol = Solution2()
tests = [
    ([1,2,3,3], [3,4,5,6], [50,10,40,70], 120),
    ([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60], 150),
    ([1,1,1], [2,3,4], [5,6,4], 6),
]

for i, (startTime, endTime, profit, ans) in enumerate(tests):
    res = sol.jobScheduling(startTime, endTime, profit)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
