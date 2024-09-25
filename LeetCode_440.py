# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def count(self, pre: int, n: int) -> int:
        """
        Count the total number of nodes in the subtree rooted at pre such that
        all the nodes are no larger than n
        """
        total = 0
        cnt = 1
        d = pre
        while d + cnt - 1 <= n:
            total += cnt
            d *= 10
            cnt *= 10
        if d <= n:
            return total + n - d + 1
        return total

    def findKthNumber(self, n: int, k: int) -> int:
        



sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
