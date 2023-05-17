# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        """Binary search.

        O(NlogM), where M = max(ranks)
        952 ms, faster than 77.42%
        """
        lo, hi = 0, max(ranks) * cars**2 + 1
        while lo < hi:
            mid = (lo + hi) // 2
            cur_cars = 0
            for r in ranks:
                cur_cars += math.isqrt(mid // r)
                if cur_cars >= cars:
                    break
            else:
                lo = mid + 1
                continue
            hi = mid
        return lo


sol = Solution()
tests = [
    ([4,2,3,1], 10, 16),
    ([5,1,8], 6, 16),
]

for i, (ranks, cars, ans) in enumerate(tests):
    res = sol.repairCars(ranks, cars)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
