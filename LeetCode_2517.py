# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_left


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        lo, hi = 0, price[-1] - price[0] + 1
        while lo < hi:
            mid = (lo + hi) // 2
            i, c = 0, 1
            while i < len(price) and c < k:
                c += 1
                i = bisect_left(price, price[i] + mid)
            if i < len(price):  # mid can be established as tastiness
                lo = mid + 1  # try a bigger tastiness
            else:
                hi = mid
        return lo - 1


sol = Solution()
tests = [
    ([13,5,1,8,21,2], 3, 8),
    ([1,3,1], 2, 2),
    ([7,7,7,7], 2, 0),
]

for i, (price, k, ans) in enumerate(tests):
    res = sol.maximumTastiness(price, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
