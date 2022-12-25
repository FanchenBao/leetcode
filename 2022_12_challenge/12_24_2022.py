# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution1:
    def numTilings(self, n: int) -> int:
        """LeetCode 790

        Follow the configurations specified in the comments. Use DP.

        O(N^2), 778 ms, faster than 6.35%
        """
        MOD = 10**9 + 7

        @lru_cache(maxsize=None)
        def solve(idx: int) -> int:
            if idx == n - 1 or idx == n:
                return 1
            if idx == n - 2:
                return 2
            # one vertical and two horizontal
            res = (solve(idx + 1) + solve(idx + 2)) % MOD
            # use tromino.
            # bottom left + top right
            # top left + bottom right
            # These two are exactly the same in terms of count
            # top left + top right
            # bottom left + bottom right
            # These two are exactly the same in terms of count
            for j in range(idx + 3, n + 1):
                res = (res + 2 * solve(j)) % MOD
            return res

        return solve(0)


class Solution2:
    def numTilings(self, n: int) -> int:
        """Bottom up DP

        It is clear from Solution1 that we can use a suffix sum to avoid
        repeated sum over a range of values. With suffix sum, we are able to
        translate Solution1 to a 1D DP.

        O(N), 29 ms, faster than 97.94% 
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        MOD = 10**9 + 7
        sufsum = 1  # when idx == n
        ss = 1  # when idx == n - 1 (2x1 board)
        s = 2  # when idx == n - 2 (2x2 board)
        for i in range(n - 3, -1, -1):
            tmp = (s + ss + sufsum * 2) % MOD
            sufsum, s, ss = (sufsum + ss) % MOD, tmp, s
        return s



sol = Solution2()
tests = [
    (3, 5),
    (1, 1),
    (4, 11),
]

for i, (n, ans) in enumerate(tests):
    res = sol.numTilings(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
