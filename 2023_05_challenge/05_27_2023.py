# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import accumulate
from functools import lru_cache


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        """LeetCode 1406

        This is almost exactly the same as the problem yesterday. DP with prefix
        sum can solve it.

        O(3N), 3698 ms, faster than 30.50%
        """
        presum = [0] + list(accumulate(stoneValue))
        N = len(stoneValue)

        @lru_cache(maxsize=None)
        def dp(idx: int) -> int:
            if idx >= N:
                return 0
            score = -math.inf
            for i in range(idx, min(N, idx + 3)):
                score = max(
                    score,
                    presum[i + 1] - presum[idx] + presum[-1] - presum[i + 1] - dp(i + 1),
                )
            return score

        alice = dp(0)
        bob = presum[-1] - alice
        if alice == bob:
            return 'Tie'
        if alice > bob:
            return 'Alice'
        return 'Bob'
        

sol = Solution()
tests = [
    ([1,2,3,7], 'Bob'),
    ([1,2,3,-9], 'Alice'),
    ([1,2,3,6], 'Tie'),
]

for i, (stoneValue, ans) in enumerate(tests):
    res = sol.stoneGameIII(stoneValue)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
