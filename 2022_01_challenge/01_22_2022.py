# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache
import math


class Solution1:
    def winnerSquareGame(self, n: int) -> bool:
        """LeetCode 1510

        The remaining number of stones can be considered as a state. We can
        cache the result as given the number of stones, can the first player
        win for all possible stone conditions. During the DFS, we are always
        looking from the perspective of the first player. Then when we
        recursively call dfs() again, its result indicates whether the second
        player will win. Thus, if the recursive dfs() is true, we have to try
        the next value for the first player. Otherwise, we know that the first
        player has already won.

        3854 ms, 18% ranking. BUT terrible memory requirement: 161 MB!!
        """

        @lru_cache(maxsize=None)
        def dfs(stones: int) -> bool:
            """return True if first player wins, otherwise False"""
            i = 1
            while i * i <= stones:
                if not dfs(stones - i * i):
                    return True
                i += 1
            return False

        return dfs(n)


class Solution2:
    def winnerSquareGame(self, n: int) -> bool:
        """Same idea as solution1, but bottom up

        Much faster than top down. 

        O(N * sqrt(N)), 1292 ms, 57% ranking.
        """
        first_wins = [False] * (n + 1)
        choices = [i * i for i in range(1, int(math.sqrt(n)) + 1)]
        for i in range(1, n + 1):
            first_wins[i] = any(not first_wins[i - c] for c in choices if c <= i)
        return first_wins[n]


class Solution3:
    def winnerSquareGame(self, n: int) -> bool:
        """Same as solution1, but start from bigger choices going down.

        This is ten times faster than from small to big. It's also faster than
        the bottom up solution.

        302 ms, 85% ranking
        """

        @lru_cache(maxsize=None)
        def dfs(stones: int) -> bool:
            """return True if first player wins, otherwise False"""
            i = int(math.sqrt(stones))
            while i >= 1:
                if not dfs(stones - i * i):
                    return True
                i -= 1
            return False

        return dfs(n)


sol = Solution3()
tests = [
    (1, True),
    (2, False),
    (4, True),
]

for i, (n, ans) in enumerate(tests):
    res = sol.winnerSquareGame(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
