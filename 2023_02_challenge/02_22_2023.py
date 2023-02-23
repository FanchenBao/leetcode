# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import accumulate
from bisect import bisect_right


class Solution1:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """LeetCode 1011

        Double binary search. Use outer binary search to find the capacity of
        the ship. Use a inner binary search to verify whether the current
        capacity is valid.

        O(logN * logN), 705 ms, faster than 25.19%
        """
        lo, hi = max(weights), sum(weights) + 1
        presum = list(accumulate(weights))
        while lo < hi:
            mid = (lo + hi) // 2
            c = d = 0
            while c < presum[-1]:
                idx = bisect_right(presum, c + mid)
                d += 1
                c = presum[idx - 1]
            if d <= days:
                hi = mid
            else:
                lo = mid + 1
        return lo



class Solution2:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """O(NlogN) also works. 777 ms, faster than 22.08%
        """
        lo, hi = max(weights), sum(weights) + 1
        while lo < hi:
            mid = (lo + hi) // 2
            d = s = 0
            for w in weights:
                if s + w < mid:
                    s += w
                else:
                    d += 1
                    s = w * int(s + w > mid)
                if d > days:
                    break
            d += int(s > 0)
            if d <= days:
                hi = mid
            else:
                lo = mid + 1
        return lo


sol = Solution2()
tests = [
    ([1,2,3,4,5,6,7,8,9,10], 5, 15),
    ([3,2,2,4,1,4], 3, 6),
    ([1,2,3,1,1], 4, 3),
]

for i, (weights, days, ans) in enumerate(tests):
    res = sol.shipWithinDays(weights, days)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
