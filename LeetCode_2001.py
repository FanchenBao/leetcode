# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution:
    def gcd(self, a: int, b: int) -> int:
        if a < b:
            a, b = b, a
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        """Fairly easy. Just to find the ratio of each width height pair. Roll
        our own GCD, which, for whatever reason, is always faster in LeetCode
        than using math.gcd.

        O(NlogK), N = len(rectangles), K = max(rectangles).
        2093 ms, faster than 86.05%
        """
        counter = Counter()
        for w, h in rectangles:
            gcd = self.gcd(w, h)
            counter[(w // gcd, h // gcd)] += 1
        return sum(v * (v - 1) // 2 for v in counter.values())


sol = Solution()
tests = [
    ([[4,8],[3,6],[10,20],[15,30]], 6),
    ([[4,5],[7,8]], 0),
]

for i, (rectangles, ans) in enumerate(tests):
    res = sol.interchangeableRectangles(rectangles)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
