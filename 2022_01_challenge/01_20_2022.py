# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """LeetCode 875

        Binary search. I have used this exact binary search method a couple of
        weeks ago in a contest (but I don't quite remember the exact question).
        We first identify the lower and higher bound of the eating speed. The
        higher bound is the max of piles. The lower bound is a bit tricky (and
        I got bitten by it). It should be the average speed by taking the sum
        of piles and divided by h. HOWEVER, if this value turns out to be zero,
        we have to force the lower bound to be one.

        Then it is just binary search, with each mid value subjected to a test
        to see whether all the bananas can be consumed within h hours.

        O(Nlog(MAX(piles))), where N = len(piles). 436 ms, 85% ranking.
        """
        lo, hi = max(sum(piles) // h, 1), max(piles)
        while lo <= hi:
            mid = (lo + hi) // 2
            if sum(math.ceil(p / mid) for p in piles) <= h:
                hi = mid - 1
            else:
                lo = mid + 1
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
