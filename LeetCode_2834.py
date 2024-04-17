# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        """
        Greedy. We want to use the smallest numbers first. We can go from 1,
        2, 3, ... all the way to target // 2. Anything more than that, we will
        have two values add up to target. Thus, the max allowed from 1 is
        target // 2. If the max allowed already exceeds n, then the answer is
        just the sum from 1 to n.

        If target // 2 is not enough, then we need to add values that are large
        enough such that when they add to 1, 2, 3... it is larger than the
        target. The first such value is going to be target itself. And we need
        n - max allowed number of them.

        O(1), 32 ms, faster than 75.00%
        """
        MOD = 10**9 + 7
        max_allowed = target // 2
        if max_allowed >= n:
            return (n + 1) * n // 2 % MOD
        return (
            (target + target + n - max_allowed - 1) * (n - max_allowed) // 2
            + (max_allowed + 1) * max_allowed // 2
        ) % MOD


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
