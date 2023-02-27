# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache
from collections import defaultdict


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """LeetCode 72

        Took a long time to realize the correct way to think about DP. I was
        worried about addition, but the worry is not warranted. When word1[i] is
        not equal to word2[j], we either replace one to match the other, which
        generates one change; or delete word1[i] or word2[j], which generates
        one change; or add a letter in before word1[i] to match word2[j] or add
        a letter before word2[j] to match word1[i], which generates one change.

        One would notice that the outcome of deleting or adding a letter is the
        same. The overall process is quite similar to LCS, with only a little
        twist.

        helper(i, j) returns the min distance between word1[i:] and word2[j:]

        O(MN), 86 ms, faster than 96.50% 
        """
        M, N = len(word1), len(word2)
        if M * N == 0:
            return max(M, N)

        @lru_cache(maxsize=None)
        def helper(i: int, j: int) -> int:
            if i == M or j == N:
                return max(M - i, N - j)
            if word1[i] == word2[j]:
                return helper(i + 1, j + 1)
            return 1 + min(helper(i + 1, j + 1), helper(i + 1, j), helper(i, j + 1))

        return helper(0, 0)

        


sol = Solution()
tests = [
    ("horse", "ros", 3),
    ("intention", "execution", 5),
    ("", "", 0,),
    ("a", "b", 1),
    ("teacher", "botcher", 3),
    ("distance", "daliance", 3),
]

for i, (word1, word2, ans) in enumerate(tests):
    res = sol.minDistance(word1, word2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
