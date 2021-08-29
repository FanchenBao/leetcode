# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache
import bisect


class Solution1:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """LeetCode 1235

        DP for sure. The question is how to we form the DP. First of all, we
        can observe that for any job that we choose to include, we can find the
        max profit of all the jobs with starting time larger or equal to the
        end time of the chosen job. This is our DP relationship. If we sort
        all the jobs by their starting time, then we can use the index of the
        sorted job list as the key for the DP. Say we choose idx = 0 for our
        first job. We then iterate through the list to find the first job with
        starting time larger or equal to the end time of job 0. Let's say that
        is job 5. Then we recursively solve the same problem by calling solve(5)
        Then, we choose job 1 and do the same algo. We continue until job 5,
        then we can stop, because the max profit starting from job 5 will
        definitely be smaller than starting from job 0, because the latter is
        the sum of job 0's profit and the max profit starting from job 5. We can
        end the loop right there. In addition, since index is the value used for
        the key for DP, we can easily cache the results. And we are done.

        Worst case time complexity is O(NlogN), 684 ms, 38% ranking.
        """
        combined = sorted(zip(startTime, endTime, profit), key=lambda tup: tup[0])
        sorted_starts = [s for s, _, _ in combined]
        N = len(combined)

        @lru_cache(None)
        def solve(idx: int) -> int:
            prof = 0
            for i in range(idx, N):
                if combined[i][0] >= combined[idx][1]:
                    break
                temp = combined[i][2]
                next_idx = bisect.bisect_left(sorted_starts, combined[i][1])
                if next_idx < N:
                    temp += solve(next_idx)
                prof = max(prof, temp)
            return prof

        return solve(0)


class Solution2:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """Bottom up solution

        Courtesy: https://leetcode.com/problems/maximum-profit-in-job-scheduling/submissions/

        dp[i] represents the max profit starting from job i towards the end
        """
        combined = sorted(zip(startTime, endTime, profit), key=lambda tup: tup[0])
        sorted_starts = [s for s, _, _ in combined]
        N = len(combined)
        dp = [0] * (N + 1)
        for i in range(N - 1, -1, -1):
            next_idx = bisect.bisect_left(sorted_starts, combined[i][1])
            dp[i] = max(combined[i][2] + dp[next_idx], dp[i + 1])
        return dp[0]


sol = Solution2()
tests = [
    ([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70], 120),
    ([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60], 150),
    ([1, 1, 1], [2, 3, 4], [5, 6, 4], 6),
]

for i, (startTime, endTime, profit, ans) in enumerate(tests):
    res = sol.jobScheduling(startTime, endTime, profit)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
