# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache
from itertools import accumulate


class Solution1:
    def stoneGameII(self, piles: List[int]) -> int:
        """LeetCode 1140

        DP can solve this problem. At each idx and M, a player can take 1, 2,
        ..., 2M piles, and find the max he/she can get at each situation. Return
        the max among all situations.

        O(N^3), 610 ms, faster than 51.61%
        """
        presum = [0] + list(accumulate(piles))
        N = len(piles)

        @lru_cache(maxsize=None)
        def dp(idx: int, M: int) -> int:
            if idx >= N:
                return 0
            res = 0
            for num_to_take in range(1, 2 * M + 1):
                res = max(
                    res,
                    # this is simplied from
                    # presum[min(N, idx + num_to_take)] - presum[idx] + presum[-1] - presum[min(N, idx + num_to_take)]
                    presum[-1] - presum[idx] - dp(idx + num_to_take, max(M, num_to_take)),
                )
            return res

        return dp(0, 1)


class Solution2:
    def stoneGameII(self, piles: List[int]) -> int:
        """Another way to do it.

        O(N^3), 425 ms, faster than 59.91%
        """
        N = len(piles)
        presum = [0] + list(accumulate(piles))

        def dp(idx: int, M: int) -> int:
            if idx >= N:
                return 0
            res = stones =0
            for i in range(idx, min(N, idx + 2 * M)):
                stones += piles[i]
                res = max(
                    res,
                    stones + presum[-1] - presum[i + 1] - dp(i + 1, max(M, i - idx + 1)),
                )
            return res

        return dp(0, 1)
        

sol = Solution2()
tests = [
    ([2,7,9,4,4], 10),
    ([1,2,3,4,5,100], 104),
]

for i, (piles, ans) in enumerate(tests):
    res = sol.stoneGameII(piles)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
