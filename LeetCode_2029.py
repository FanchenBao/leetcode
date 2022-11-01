# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        c = Counter(s % 3 for s in stones)
        if c[1] == c[2] == 0:
            return False
        if c[0] % 2 == 0:
            if c[1] == 0:
                return c[1] > c[2] - 1  # A takes 2 first
            if c[2] == 0:
                return c[2] > c[1] - 1  # A takes 1 first
            return c[1] > c[2] - 1 or c[2] > c[1] - 1
        if c[1] == 0:
            return c[2] - 2 > c[1]  # A takes 2 first
        if c[2] == 0:
            return c[1] - 2 > c[2]  # A takes 1 first
        return c[2] - 2 > c[1] or c[1] - 2 > c[2]


sol = Solution()
tests = [
    ([2, 1], True),
    ([2], False),
    ([5, 1, 2, 3, 4], False),
]

for i, (stones, ans) in enumerate(tests):
    res = sol.stoneGameIX(stones)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
