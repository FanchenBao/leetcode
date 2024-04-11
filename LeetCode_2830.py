# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        """
        dp[i] is the max earning when selling an offer whose end is i. When
        selling this offer, we cannot sell any other offers whose end is
        within the start and end of the current offer. Thus, we need to find
        the max earning when selling at the house at position start - 1.

        dp[i] = max(dp[i], current_earning + dp[start - 1])

        After the dp computation (or not, if the current house is not an end
        to an offering), we have to keep dp as a prefix max.

        O(NlogN + N + M), 1078 ms, faster than 60.40%

        NOTE: there is another implementation of this solution that uses
        extra space to reduce the run time to O(N + M). Using the extra space
        as a mapping to quickly find what offerings are associated with a
        specific house, we do not need to sort. It's not difficult to implement
        and I will skip it.
        """
        dp = [0] * n
        offers.sort(key=lambda tup: tup[1])
        idx = 0
        for i in range(n):
            while idx < len(offers) and offers[idx][1] == i:
                j = offers[idx][0]
                dp[i] = max(dp[i], offers[idx][2] + (dp[j - 1] if j - 1 >= 0 else 0))
                idx += 1
            if i - 1 >= 0:
                dp[i] = max(dp[i], dp[i - 1])
        return dp[-1]


sol = Solution()
tests = [
    (
        4,
        [
            [0, 0, 6],
            [1, 2, 8],
            [0, 3, 7],
            [2, 2, 5],
            [0, 1, 5],
            [2, 3, 2],
            [0, 2, 8],
            [2, 3, 10],
            [0, 3, 2],
        ],
        16,
    ),
]

for i, (n, offers, ans) in enumerate(tests):
    res = sol.maximizeTheProfit(n, offers)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
