# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter
import math
from itertools import accumulate
from bisect import bisect_left


class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        flowers.sort()
        num_full = 0
        j = len(flowers) - 1
        while flowers[j] >= target:
            num_full += 1
            j -= 1
        presum = list(accumulate(flowers))
        for add_full in range(j + 2):
            full_needed = target * add_full - (presum[j] - presum[-1 - i])
            flowers_remain = newFlowers - full_needed
            if flowers_remain < 0:
                break
            lo, hi = uniqs[0], target - 1
            while lo < hi:
                mid = (lo + hi + 1) // 2
                idx = bisect_left(uniqs, mid)
                partial_needed = 0 if idx == 0 else mid *  - presum[idx - 1]


        


sol = Solution()
tests = [
    # ([1,3,1,1], 7, 6, 12, 1, 14),
    ([2,4,5,3], 10, 5, 2, 6, 30),
]

for i, (flowers, newFlowers, target, full, partial, ans) in enumerate(tests):
    res = sol.maximumBeauty(flowers, newFlowers, target, full, partial)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
