# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache
from collections import Counter, defaultdict


class Solution1:
    def tallestBillboard(self, rods: List[int]) -> int:
        """TLE big time.
        """
        N = len(rods)
        cur_rods = []
        res = 0

        @lru_cache(maxsize=None)
        def solve(idx: int, rem: int) -> bool:
            if rem == 0:
                return True
            if idx >= len(cur_rods) or rem < 0:
                return False
            return solve(idx + 1, rem) or solve(idx + 1, rem - cur_rods[idx])

        for state in range((1 << N) - 1, -1, -1):
            cur_rods = []
            for i in range(N):
                if (1 << i) & state:
                    cur_rods.append(rods[i])
            total = sum(cur_rods)
            if total % 2:  # odd, impossible
                continue
            h = total // 2
            if solve(0, h):
                res = max(res, h)
                solve.cache_clear()  # have to reset cache, but it leads to TLE
        return res


class Solution2:
    def tallestBillboard(self, rods: List[int]) -> int:
        """Fail

        This is the DP solution from the official solution. It is indeed very
        hard to identify the state. We use dp[i] to represent the taller size
        of the two rods with the difference between the two rods being i.

        As we go from rods one by one, the current rod can be applied to all the
        previous dp values to either create a new dp[diff], or to update an
        existing dp[diff] that has smaller size for the taller rod. We go
        through the entire rods and we will have the answer in dp[0]

        O(NM), where N = len(rods), M is the total number of differences that
        can be generated between any rod combinations. 569 ms, faster than 64.58%
        """
        dp = defaultdict(int)
        dp[0] = 0  # starting state is two rods with 0 diff, and the taller rod has 0 height
        for i, r in enumerate(rods):
            new_dp = dp.copy()  # we do not want to change the value in the previous dp when computing the current dp
            for diff, taller in dp.items():
                new_dp[diff + r] = max(new_dp[diff + r], taller + r)
                shorter = dp[diff] - diff
                new_diff = abs(taller - (shorter + r))
                new_taller = max(shorter + r, taller)
                new_dp[new_diff] = max(new_dp[new_diff], new_taller)
            dp = new_dp
        return dp[0]



sol = Solution2()
tests = [
    ([1,2,3,6], 6),
    ([1,2,3,4,5,6], 10),
    ([1,2,3,4,5,6,7], 14),
    ([1,2], 0),
    ([102,101,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100], 900),
    ([518,99,365,338,800,869,917,386,129,382,116], 2219),
    ([3,4,3,3,2], 6),
]

for i, (rods, ans) in enumerate(tests):
    res = sol.tallestBillboard(rods)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
