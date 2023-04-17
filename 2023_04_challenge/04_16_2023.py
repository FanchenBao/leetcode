# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache
from collections import Counter


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        """LeetCode 1639

        First of all, one has to understand the problem well. That was my
        initial mistake, as I misunderstood what the problem was asking for.

        Then for DP to work, we need a certain order for us to traverse through
        all the states. In this problem, the order is NOT the order in words,
        but the order of indices used from words, regardless of the actual words
        used.

        Thus, we must know what choices do we have at each index of all the
        words. We can use a list of counts, where counts[i] is a counter of all
        letters appearing at the ith index of all words.

        Then for each pair of i, j, where j is the current position in target
        to match, we can decide whether there is any letter in words that can
        match by checking counts[i][target[j]] > 0.

        Of course, we can also choose not to use the ith index.

        With these two conditions, the actual DP relation is not that complex to
        come up.

        O(K + MN), where K is the total number of letters in words, M is the
        length of the longest word in words, and N is the size of target.

        3264 ms, faster than 26.85%
        """
        MOD = 10**9 + 7
        # counts[i] is a counter that shows the number of letters that occur at
        # position i in every word, if possible.
        counts = []
        for word in words:
            for i, w in enumerate(word):
                if i == len(counts):
                    counts.append(Counter())
                counts[i][w] += 1

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            """dp[i][j] is the total number of ways to form target[j:] using
            counts[i:]
            """
            if i >= len(counts) and j < len(target):
                return 0
            if j == len(target):
                return 1
            res = (dp(i + 1, j) + counts[i][target[j]] * dp(i + 1, j + 1)) % MOD
            return res

        return dp(0, 0)
        

sol = Solution()
tests = [
    (["acca","bbbb","caca"], "aba", 6),
    (["abba","baab"], "bab", 4),
]

for i, (words, target, ans) in enumerate(tests):
    res = sol.numWays(words, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
