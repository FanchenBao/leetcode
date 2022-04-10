# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter
import math


class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        counter = Counter(flowers)
        uniqs = [0] + sorted(counter) + [math.inf]
        lo, hi = 1, len(uniqs) - 2
        while uniqs[hi] >= target:
            hi -= 1
        while lo < hi:
            unit_inc_full = full / (target - uniqs[hi])
            unit_inc_partial = partial / counter[uniqs[lo]]
            if unit_inc_full >= unit_inc_partial and newFlowers >= target - uniqs[hi]:
                newFlowers -= target - uniqs[hi]
                hi -= 1
            elif unit_inc_partial > unit_inc_full and newFlowers >= couter[uniqs[lo]]:
                newFlowers -= counter[uniqs[lo]]
                uniqs[lo] += 1
                if uniqs[lo + 1] == uniqs[lo]:
                    counter[uniqs[lo + 1]] += counter[uniqs[lo]]
                    lo += 1
            else:
                break
        return full * (len(uniqs) - hi - 2) + partial * uniqs[lo - 1]



        


sol = Solution()
tests = [
    ([1,1,2,3,5], 1),
    ([1,1,2,2,3,3], 2),
    ([1,2,3,3,4,4,5,5,6], 1),
    ([1], 1),
    ([], 0),
    ([1,1,1,1,1], 5),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.minDeletion(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
