# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache
from bisect import bisect_right


class Solution1:
    def canCross(self, stones: List[int]) -> bool:
        """LeetCode 403

        Standard DP with binary search at each step to find whether a next jump
        is possible.

        O(N^2logN), 144 ms, faster than 81.91%, where N = len(stones)
        """
        if stones[1] != 1:
            return False
        N = len(stones)

        @lru_cache(maxsize=None)
        def dp(idx: int, k: int) -> bool:
            if idx == N - 1:
                return True
            # op1, jump k
            i1 = bisect_right(stones, stones[idx] + k)
            if i1 - 1 < N and stones[i1 - 1] == stones[idx] + k and dp(i1 - 1, k):
                return True
            # op2, jump k - 1
            if k - 1 > 0:
                i2 = bisect_right(stones, stones[idx] + k - 1)
                if i2 - 1 < N and stones[i2 - 1] == stones[idx] + k - 1 and dp(i2 - 1, k - 1):
                    return True
            # op3, jump k + 1
            i3 = bisect_right(stones, stones[idx] + k + 1)
            if i3 - 1 < N and stones[i3 - 1] == stones[idx] + k + 1 and dp(i3 - 1, k + 1):
                return True
            return False

        return dp(1, 1)


class Solution2:
    def canCross(self, stones: List[int]) -> bool:
        """No need to binary search, because we can simply use a mapping to
        check whether a stone exists.

        O(N^2), 101 ms, faster than 97.46%
        """
        if stones[1] != 1:
            return False
        N = len(stones)
        stone_map = {st: i for i, st in enumerate(stones)}

        @lru_cache(maxsize=None)
        def dp(idx: int, k: int) -> bool:
            if idx >= N:
                return False
            if idx == N - 1:
                return True
            for kk in range(k - 1, k + 2):
                if kk > 0 and dp(stone_map.get(stones[idx] + kk, math.inf), kk):
                    return True
            return False

        return dp(1, 1)
        

sol = Solution2()
tests = [
    ([0,1,3,5,6,8,12,17], True),
    ([0,1,2,3,4,8,9,11], False),
]

for i, (stones, ans) in enumerate(tests):
    res = sol.canCross(stones)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
