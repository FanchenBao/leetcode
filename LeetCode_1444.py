# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache
from itertools import accumulate


class Solution:
    def query(self, tl_i: int, tl_j: int, br_i: int, br_j: int) -> int:
        base = self.prefix2d[br_i][br_j]
        left_remove = self.prefix2d[br_i][tl_j - 1] * int(tl_j - 1 >= 0)
        top_remove = self.prefix2d[tl_i - 1][br_j] * int(tl_i - 1 >= 0)
        diag_add = self.prefix2d[tl_i - 1][tl_j - 1] * int(tl_j - 1 >= 0) * int(tl_i - 1 >= 0)
        return base - left_remove - top_remove + diag_add

    def ways(self, pizza: List[str], k: int) -> int:
        """Use 2D prefix sum to describe the pizza, such that we can obtain the
        number of apples in any given range in O(1)

        Then we use DP to obtain the total number of cuts given the top left
        coordinates and the remaining number of cuts.

        O(MN + MNK(M + N)), 642 ms, faster than 46.63%
        """
        MOD = 10**9 + 7
        M, N = len(pizza), len(pizza[0])

        self.prefix2d = []
        for row in pizza:
            self.prefix2d.append(list(accumulate(int(it == 'A') for it in row)))
            if len(self.prefix2d) > 1:
                for j in range(N):
                    self.prefix2d[-1][j] += self.prefix2d[-2][j]

        @lru_cache(maxsize=None)
        def dp(i: int, j: int, rem_cuts: int) -> int:
            if not rem_cuts:
                return int(self.query(i, j, M - 1, N - 1) > 0)
            res = 0
            # vertical cuts. j:q + 1 are the cols to be given away
            for q in range(j, N - 1):
                if self.query(i, j, M - 1, q) > 0:
                    res += dp(i, q + 1, rem_cuts - 1)
            # horizontal cuts. i:p + 1 are the rows to be given away
            for p in range(i, M - 1):
                if self.query(i, j, p, N - 1) > 0:
                    res += dp(p + 1, j, rem_cuts - 1)
            return res

        return dp(0, 0, k - 1) % MOD

sol = Solution()
tests = [
    (["A..","AAA","..."], 3, 3),
    (["A..","AA.","..."], 3, 1),
    (["A..","A..","..."], 1, 1),
]

for i, (pizza, k, ans) in enumerate(tests):
    res = sol.ways(pizza, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
