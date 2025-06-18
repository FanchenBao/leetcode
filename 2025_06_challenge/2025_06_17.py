# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        """
        LeetCode 3405 (Fail)

        I am surprised that I solved this last time in January 5th, 2025. I am
        not able to solve it again today.

        The idea is that whatever k indices that we choose, there will always
        be n - k number of independent entities. An entity is a subarray
        consisting of the same value.

        The extreme case is that none of the k pairs overlap. Thus, we have
        n - 2 * k + k = n - k independent entities.

        Now, if we allow some pairs to overlap. When overlap happens, we lose
        one entity from the pairs, but we also gain an entity from the
        overlapped index. Thus, the total number of independent entities
        remain the same.

        We also know that there are (n - 1)C(k) number of ways to place the
        k indices (we cannot put k at position 0).

        For each way, we have m choices for the first position, and m - 1 ways
        for each of the remaining (n - k - 1) entities.

        Thus, the solution is m * (m - 1)^*(n - k - 1) * (n - 1)C(k)
        """
        MOD = 1000000007
        comb = math.comb(n - 1, k) % MOD
        return m * pow(m - 1, n - k - 1, mod=MOD) * comb % MOD


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
