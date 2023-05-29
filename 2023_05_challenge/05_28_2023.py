# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache
from bisect import bisect_left, bisect_right


class Solution1:
    def minCost(self, n: int, cuts: List[int]) -> int:
        """TLE
        """
        memo = {}

        def dp(lo: int, hi: int, idx: int) -> int:
            if (lo, hi, idx) not in memo:
                memo[(lo, hi, idx)] = hi - lo
                left = right = math.inf
                for j in cuts:
                    if lo < j < idx:
                        left = min(left, dp(lo, idx, j))
                    elif idx < j < hi:
                        right = min(right, dp(idx, hi, j))
                if left == math.inf:
                    left = 0
                if right == math.inf:
                    right = 0
                memo[(lo, hi, idx)] += left + right
            return memo[(lo, hi, idx)]

        return min(dp(0, n, i) for i in cuts)


class Solution2:
    def minCost(self, n: int, cuts: List[int]) -> int:
        """LeetCode 1547

        I was thinking about it too complicated. Instead of making it a three
        level DP, we can simply make it a two-level, where dp(lo, hi) finds the
        min cost of cutting the wood from position lo to hi. We simply iterate
        through all cuts and make the cut if it lands in between lo and hi.

        O(M^3), where M = len(cuts), 1302 ms, faster than 52.68%
        """
        @lru_cache(maxsize=None)
        def dp(lo: int, hi: int) -> int:
            cost = math.inf
            for i in cuts:
                if lo < i < hi:
                    cost = min(cost, hi - lo + dp(lo, i) + dp(i, hi))
            return 0 if cost == math.inf else cost

        return dp(0, n)


class Solution3:
    def minCost(self, n: int, cuts: List[int]) -> int:
        """This is the official solution, where instead of dp on the actual
        positions of the rod, we dp on the indices of cuts. This shall reduce
        the amount of computation, because we don't have to iterate through cuts
        and check for availability each time. We simply iterate through indices
        of cuts.

        O(M^3), 1068 ms, faster than 63.69% 
        """
        sorted_cuts = [0] + sorted(cuts) + [n]  # important step

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            cost = math.inf
            for k in range(i + 1, j):
                cost = min(cost, sorted_cuts[j] - sorted_cuts[i] + dp(i, k) + dp(k, j))
            return 0 if cost == math.inf else cost

        return dp(0, len(sorted_cuts) - 1)


sol = Solution3()
tests = [
    (7, [1,3,4,5], 16),
    (9, [5,6,1,4,2], 22),
]

for i, (n, cuts, ans) in enumerate(tests):
    res = sol.minCost(n, cuts )
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
