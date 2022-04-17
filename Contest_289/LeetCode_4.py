# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter
import math
from itertools import accumulate
from bisect import bisect_left


class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        """Hint

        So many edge cases!!!

        I took a look at the hints. Although I got the idea, the implementation
        was still full of problems. The main issue was the edge cases that I
        failed to take into consideration. I have marked them with "IMPORTANT"
        in the code.

        This problem is pretty darn hard.

        O(NlogN), 3715 ms, 28.49%
        """
        flowers.sort()
        num_full = 0
        j = len(flowers) - 1
        while j >= 0 and flowers[j] >= target:
            num_full += 1
            j -= 1
        presum = list(accumulate(flowers))
        res = 0
        for add_full in range(j + 2):
            # IMPORTANT: when j < add_full, i.e. the entire subarray from start
            # to j are turned into complete flowers, we cannot use
            # presum[j - add_full].
            full_needed = target * add_full - (
                presum[j] - (presum[j - add_full] if j >= add_full else 0)
            )
            flowers_remain = newFlowers - full_needed
            if flowers_remain < 0:
                break
            # IMPORTANT: if all flowers have been converted to complete, there
            # is no incomplete flower
            if add_full + num_full == len(flowers):
                lo = hi = 0
            else:
                lo, hi = flowers[0], target - 1
                while lo < hi:
                    mid = (lo + hi + 1) // 2
                    idx = bisect_left(flowers, mid)
                    if idx == 0:
                        partial_needed = 0
                    else:
                        # IMPORTANT: if the right bound for flowers that can be
                        # increased to mid is lower than idx, then we
                        # can theoretically increase all the flowers up till the
                        # right bound to mid. In other words, in this situation,
                        # the binary search result idx should not be used.
                        if idx > j - add_full:
                            idx = j - add_full + 1
                        partial_needed = mid * idx - presum[idx - 1]
                    if partial_needed <= flowers_remain:
                        lo = mid
                    else:
                        hi = mid - 1
            res = max(
                res,
                (add_full + num_full) * full + (lo * partial if lo == hi else 0),
            )
        return res


sol = Solution()
tests = [
    ([1,3,1,1], 7, 6, 12, 1, 14),
    ([2,4,5,3], 10, 5, 2, 6, 30),
    ([18,16,10,10,5], 10, 3, 15, 4, 75),
    ([5,5,15,1,9], 36, 12, 9 ,2, 58),
    ([8,10,13,10], 84, 20, 4, 2, 50),
    ([10,9,16,14,6,5,11,12,17,2,11,15,1], 80, 14, 15, 1, 195),
]

for i, (flowers, newFlowers, target, full, partial, ans) in enumerate(tests):
    res = sol.maximumBeauty(flowers, newFlowers, target, full, partial)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
