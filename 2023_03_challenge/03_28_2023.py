# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_right


class Solution1:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """LeetCode 983

        DP with binary search.

        O(NlogN), 48 ms, faster than 60.78% 
        """
        days = [0] + days
        N = len(days)
        dp = [math.inf] * N
        dp[0] = 0
        for i in range(1, N):
            for d, c in zip([1, 7, 30], costs):
                j = bisect_right(days, days[i] - d)
                if j > 0:
                    j -= 1
                dp[i] = min(dp[i], c + dp[j])
        return dp[-1]


class Solution2:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """No need to binary search, because the max amount of days is only 365.
        We can literally list every one of them

        O(max(days)), 50 ms, faster than 52.73%
        """
        dp = [math.inf] * (days[-1] + 1)
        dp[0] = 0
        dayset = set(days)
        for i in range(1, days[-1] + 1):
            if i not in dayset:
                dp[i] = dp[i - 1]
            else:
                for d, c in zip([1, 7, 30], costs):
                    dp[i] = min(dp[i], c + dp[max(i - d, 0)])
        return dp[-1]


sol = Solution2()
tests = [
    ([1,4,6,7,8,20], [2,7,15], 11),
    ([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15], 17),
    ([1], [15,2,7], 2),
]

for i, (days, costs, ans) in enumerate(tests):
    res = sol.mincostTickets(days, costs)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
