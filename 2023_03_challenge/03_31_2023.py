# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution1:
    def ways(self, pizza: List[str], k: int) -> int:
        """LeetCode 1444

        DP, with each state characterized by i, j, cuts, where i, j are the
        indices on pizza and cuts is the number of remaining cuts available.

        O(MNK(M + N)), 187 ms, faster than 93.23%
        """
        MOD = 10**9 + 7
        M, N = len(pizza), len(pizza[0])

        @lru_cache(maxsize=None)
        def helper(i: int, j: int, cuts: int) -> int:
            if cuts == 0:
                return int(any('A' in pizza[p][j:] for p in range(i, M)))
            if i == M - 1 and j == N - 1:
                return 0
            res = 0
            # cut horizontally
            has_apple = False
            for p in range(i, M - 1):
                if not has_apple and 'A' in pizza[p][j:]:
                    has_apple = True
                if has_apple:
                    tmp = helper(p + 1, j, cuts - 1)
                    if tmp > 0:
                        res = (res + tmp) % MOD
            # cut vertically
            has_apple = False
            for q in range(j, N - 1):
                if not has_apple and any('A' == pizza[ii][q] for ii in range(i, M)):
                    has_apple = True
                if has_apple:
                    tmp = helper(i, q + 1, cuts - 1)
                    if tmp > 0:
                        res = (res + tmp) % MOD
            return res

        return helper(0, 0, k - 1)


class Solution2:
    def ways(self, pizza: List[str], k: int) -> int:
        """Bottom up. Cannot figure it out all by myself, so this is according
        to the official solution.

        Very challenging to get bottom up right.

        O(MNK(M + N)), 264 ms, faster than 54.07%
        """
        MOD = 10**9 + 7
        M, N = len(pizza), len(pizza[0])
        # build a 2D prefix sum
        apples = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                apples[i][j] = int(pizza[i][j] == 'A') + apples[i + 1][j] + apples[i][j + 1] - apples[i + 1][j + 1]

        # DP. Find the number of ways to cut when there are q number of pieces
        # remaining to cut and the pizza starts at (i, j)
        dp = [[0] * N for _ in range(M)]
        for i in range(M - 1, -1, -1):  # initialize DP
            for j in range(N - 1, -1, -1):
                dp[i][j] = int(apples[i][j] > 0)

        for _ in range(2, k + 1):
            tmp = [[0] * N for _ in range(M)]
            for i in range(M - 1, -1, -1):
                for j in range(N - 1, -1, -1):
                    for ii in range(i + 1, M):  # horizontal cut
                        if apples[i][j] - apples[ii][j] > 0:
                            tmp[i][j] = (tmp[i][j] + dp[ii][j]) % MOD
                    for jj in range(j + 1, N):  # vertical cut
                        if apples[i][j] - apples[i][jj] > 0:
                            tmp[i][j] = (tmp[i][j] + dp[i][jj]) % MOD
            dp = tmp
        return dp[0][0]


class Solution3:
    def ways(self, pizza: List[str], k: int) -> int:
        """Top down DP with 2D prefix sum to simplify the logic of checking
        whether a cut is legal.

        228 ms, faster than 65.45%
        """
        MOD = 10**9 + 7
        M, N = len(pizza), len(pizza[0])
        # build a 2D prefix sum
        apples = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                apples[i][j] = int(pizza[i][j] == 'A') + apples[i + 1][j] + apples[i][j + 1] - apples[i + 1][j + 1]

        @lru_cache(maxsize=None)
        def helper(i: int, j: int, cuts: int) -> int:
            if cuts == 0:
                return int(apples[i][j] > 0)
            res = 0
            # cut horizontally
            for p in range(i + 1, M):
                if apples[i][j] - apples[p][j] > 0:
                    tmp = helper(p, j, cuts - 1)
                    if tmp > 0:
                        res = (res + tmp) % MOD
            # cut vertically
            for q in range(j + 1, N):
                if apples[i][j] - apples[i][q] > 0:
                    tmp = helper(i, q, cuts - 1)
                    if tmp > 0:
                        res = (res + tmp) % MOD
            return res

        return helper(0, 0, k - 1)



sol = Solution3()
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
