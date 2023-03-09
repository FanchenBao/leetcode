# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """LeetCode 875

        Binary search

        O(NlogM), where M = max(piles), 622 ms, faster than 13.15%
        """
        lo, hi = 1, max(piles) + 1
        while lo < hi:
            mid = (lo + hi) // 2
            cur_h = sum(p // mid + int(p % mid != 0) for p in piles)
            if cur_h > h:
                lo = mid + 1
            else:
                hi = mid
        return lo


sol = Solution()
tests = [
    ([3,6,7,11], 8, 4),
    ([30,11,23,4,20], 5, 30),
    ([30,11,23,4,20], 6, 23),
    ([312884470], 968709470, 1),
]

for i, (piles, h, ans) in enumerate(tests):
    res = sol.minEatingSpeed(piles, h)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
