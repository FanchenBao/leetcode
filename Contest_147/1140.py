#! /usr/bin/env python3
from typing import List, Tuple, Dict
from random import randint
from functools import lru_cache

"""08/02/2019

Solution1:
Naive recursion. We find the max_stone a player can get by going through
all pile options he can try. We do this alternatively for each player.
Specifically, for Alex's first step, he can either take one pile or two piles.
Then we compute the max_stone Lee can take after Alex takes one pile, since we
need Lee to play optimally. For that, we can get Alex's stone if he chooses
one pile. Similarly, we get Alex's stone if he chooses two piles. We compare
the two and take the bigger as the max_stone Alex can get, when Lee always plays
optimally.

As I was writing the explanation above, I definitely smelled some DP. Will code
the DP solution tomorrow.

Solution2:
Although I said tomorrow earlier, I couldn't wait to drop the memoization
solution right now. It took a bit longer to code than I had expected, because
I didn't realize the dp array has to be 2D. Basically, we record the max_stone
achieved by a player at each position i of piles. However, since at i, there
could be different M value, we have to consider max_stone at position i for each
M value (the larger M, the more options there is). Therefore, we have to create
a 2D array, where row represents M value and col position i. Memoization clocked
in at 164 ms, 26.18%.

This time seriously, I will have to consider the bottom-up solution tomorrow.

Solution3:
DP solution. It took me a while to finally write it up, but the basic intuition
was the same as Solution2. This one clocked at 100 ms, 54.38%.

From discussion, I learned that we can also use a dictionary to construct the
DP array, but the performance was about the same. However, the actual discussion
post used lru_cache to automatically create a dictionary for memoization
purpose, allowing one to write memoization without having to provide the cache
himself. Never heard of lru_cache before. See the solution with lru_cache in use
https://leetcode.com/problems/stone-game-ii/discuss/345230/Python-DP-Solution

Solution4:
My attempt at copying lee215's solution. Boy oh boy it clocked at 60 ms. My deer
sweet GOD!
"""


class Solution1:
    def stoneGameII(self, piles: List[int]) -> int:
        return self.aux(piles, 1)

    def aux(self, piles: List[int], M: int) -> int:
        max_stone: int = 0
        for X in range(min(2 * M, len(piles))):
            max_stone = max(
                max_stone, sum(piles) - self.aux(piles[X + 1 :], max(M, X + 1))
            )
        return max_stone


class Solution2:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = [[0] * len(piles) for _ in range(len(piles))]  # 2D array for DP
        return self.aux(piles, 1, dp, 0)

    def aux(
        self, piles: List[int], M: int, dp: List[List[int]], s: int
    ) -> int:
        try:
            if not dp[M][s]:  # For each position s, we have to also consider M
                for i in range(s, min(s + 2 * M, len(piles))):
                    dp[M][s] = max(
                        dp[M][s],
                        sum(piles[s:])
                        - self.aux(piles, max(M, i - s + 1), dp, i + 1),
                    )
            return dp[M][s]
        except IndexError:
            return 0


class Solution3:
    def stoneGameII(self, piles: List[int]) -> int:
        plen: int = len(piles)
        new_piles: List[int] = [0] + piles  # add a dummy
        # dp = [[0] * (plen + 1) for _ in range(plen + 1)]  # 2D array for DP
        dp: Dict[Tuple[int, int], int] = dict()
        cum_sum: int = 0
        for j in range(plen, 0, -1):
            cum_sum += new_piles[j]  # simple optimization
            for M in range(1, plen + 1):
                if M * 2 >= plen - j + 1:
                    dp[(M, j)] = cum_sum
                else:
                    dp[(M, j)] = cum_sum - min(
                        dp[(max(X, M), j + X)] for X in range(1, M * 2 + 1)
                    )
        return dp[(1, 1)]


class Solution4:
    def stoneGameII(self, piles: List[int]) -> int:
        plen = len(piles)
        sum_piles = piles[:]
        for i in range(plen - 2, -1, -1):
            sum_piles[i] += sum_piles[i + 1]

        @lru_cache(None)
        def dp(M: int, s: int) -> int:
            if M * 2 >= plen - s:  # player can take all remaining piles
                return sum_piles[s]
            # Player cannot take all piles, thus we have to list all the max
            # piles the next player can take if the current player takes 1, 2,
            # ..., 2 * M piles, and choose the min of these maxes to find the
            # max piles current player can take even if the next player plays
            # optimally.
            return sum_piles[s] - min(
                dp(max(M, X), s + X) for X in range(1, M * 2 + 1)
            )

        return dp(1, 0)


length = 50
t = 100
for _ in range(t):
    piles = [randint(1, 5) for _ in range(length)]
    # print(piles)
    sol3 = Solution3()
    sol4 = Solution4()
    res3 = sol3.stoneGameII(piles)
    res4 = sol4.stoneGameII(piles)
    if res3 != res4:
        print(f"res3 = {res3}\nres4 = {res4}\n{piles}")
    # print(res2)
