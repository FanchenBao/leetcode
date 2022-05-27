# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache
import math


class Solution1:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        """I am surprised that I solved this one. It is just DP, but in order
        to pass the OJ, we need to use one more trick that is a prefix sum to
        quickly find the number of white tiles in any range within floor.

        The DP idea is pretty straightforward. dp[i][j] is the max number of
        white tiles uptil floor[i] that j number of carpets can cover. For each
        new tile, if it is black, there is nothing to do. We simply copy
        everything from the previous row. Otherwise, we have two choices. Either
        a carpet is used to cover the current white tile. We find out the max
        extension the carpet can reach from the current white tile to the left.
        We count the number of whites that can be covered in this range. Say
        this range is k to i. Then we add that to dp[k - 1][j - 1] to find out
        the max number of white tiles that can be covered when covering the
        current white. Keep doing this, then we return the number of white tiles
        minus dp[-1][-1] 

        O(MN), where M = len(floor), N = numCarpets. 6435 ms, faster than 46.89%
        """
        M, N = len(floor), numCarpets
        dp = [[0] * (N + 1) for _ in range(M)]
        acc_ones = [1] if floor[0] == '1' else [0]
        for i in range(1, M):
            acc_ones.append(acc_ones[-1] + (floor[i] == '1'))
        if floor[0] == '1':
            for j in range(1, N + 1):
                dp[0][j] = 1
        for i in range(1, M):
            for j in range(1, N + 1):
                dp[i][j] = dp[i - 1][j]
                if floor[i] == '1':
                    k = max(i - carpetLen + 1, 0)
                    dp[i][j] = max(
                        dp[i][j],
                        (acc_ones[i] - acc_ones[k - 1] + dp[k - 1][j - 1]) if k > 0 else acc_ones[i],
                    )
        return acc_ones[-1] - dp[-1][-1]


class Solution2:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:

        @lru_cache(maxsize=None)
        def dp(idx: int, carp: int) -> int:
            if idx < 0:
                return 0
            return min(
                int(floor[idx]) + dp(idx - 1, carp),  # don't cover
                dp(idx - carpetLen, carp - 1) if carp else math.inf
            )

        return dp(len(floor) - 1, numCarpets)
 


sol = Solution2()
tests = [
    ("10110101",  2,  2, 2),
    ("11111",  2,  3, 0),
    ("1110111", 2, 1, 4),
]

for i, (floor, numCarpets, carpetLen, ans) in enumerate(tests):
    res = sol.minimumWhiteTiles(floor, numCarpets, carpetLen)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
