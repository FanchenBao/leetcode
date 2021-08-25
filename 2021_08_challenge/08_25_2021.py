# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """LeetCode 633

        This is basically a two-sum problem dressed in squares. We first find
        the range for a and b, and then use the two pointer method to squeeze
        closer to the solution.

        O(sqrt(c)), 528 ms, 17% ranking.
        """
        a, b = 0, int(math.sqrt(c))
        while a <= b:
            if a**2 + b**2 == c:
                return True
            if a**2 + b**2 < c:
                a += 1
            else:
                b -= 1
        return False


sol = Solution()
tests = [
    (5, True),
    (3, False),
    (4, True),
    (2, True),
    (1, True),
]

for i, (c, ans) in enumerate(tests):
    res = sol.judgeSquareSum(c)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
