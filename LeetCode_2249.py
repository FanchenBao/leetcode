# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        lats = set()
        for x, y, r in circles:
            for i in range(x - r, x + r + 1):
                for j in range(y - r, y + r + 1):
                    if (i - x)**2 + (j - y)**2 <= r * r:
                        lats.add((i, j))
        return len(lats)


sol = Solution()
tests = [
    ([[2,2,2],[3,4,1]], 16),
    ([[2,2,1]], 5),
]

for i, (circles, ans) in enumerate(tests):
    res = sol.countLatticePoints(circles)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
