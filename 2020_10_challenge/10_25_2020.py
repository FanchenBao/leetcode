# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        """73% ranking. Typical DP solution.
        """
        outcome = [False] * (n + 1)
        square_num = set(i * i for i in range(1, int(math.sqrt(n)) + 1))
        for i in range(1, n + 1):
            if i in square_num:
                outcome[i] = True
            else:
                # only if all the next move (Bob's move) results in True can
                # we set current move to False
                outcome[i] = not all(outcome[i - sn] for sn in square_num if sn < i)
        return outcome[n]


sol = Solution()
tests = [
    (1, True),
    (2, False),
    (3, True),
    (4, True),
    (5, False),
    (6, True),
    (7, False),
    (17, False),
    (700, True),
]

for i, (n, ans) in enumerate(tests):
    res = sol.winnerSquareGame(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
