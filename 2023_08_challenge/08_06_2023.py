# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution1:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        """LeetCode 920

        Failed BIG BIG time. 3 hours!! Not able to solve. And the solution is
        actually pretty simple, but I simply could not wrap my head around the
        DP state.

        O(N * GOAL), 58 ms, faster than 74.44% 
        """
        MOD = 10**9 + 7
        # dp[i][j] is the number of ways to fit any j unique songs
        # (from n total songs) into a playlist of length i
        dp = [0] * (n + 1)
        # given 0 unique songs, we have 1 way to fit a playlist of length 0
        dp[0] = 1
        for i in range(1, goal + 1):
            tmp = [0] * (n + 1)
            # dp[i][j] can be computed in two ways.
            # First, the jth song added is a new song. Then for each new song
            # added, we have dp[i - 1][j - 1] number of ways. There are
            # n - j + 1 number of new songs at the moment, thus this way adds
            # dp[i - 1][j - 1] * (n - j + 1) number of ways
            # Second, the jth song is a repeated song. Then for each allowed
            # repeated song, we have dp[i - 1][j] ways to generating a playlist.
            # How many songs are we allowed to repeat. Since we must repeat with
            # a gap of k, that means we cannot repeat any of the last k songs
            # and those k songs are all unique. Thus, the songs allowed to repeat
            # is j - k.
            for j in range(1, min(i, n) + 1):
                tmp[j] = dp[j - 1] * (n - j + 1) % MOD
                if j > k:
                    tmp[j] = (tmp[j] + dp[j] * (j - k)) % MOD
            dp = tmp
        return dp[-1]





sol = Solution2()
tests = [
    (3, 3, 1, 6),
    (2, 3, 0, 6),
    (2, 3, 1, 2),
]

for i, (n, goal, k, ans) in enumerate(tests):
    res = sol.numMusicPlaylists(n, goal, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
