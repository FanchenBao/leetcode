# from pudb import set_trace; set_trace()
from typing import List
from bisect import bisect_left


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        """TLE"""
        candies.sort()
        total, N = sum(candies), len(candies)
        lo, hi = candies[0], candies[-1]
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid * k > total:
                hi = mid - 1
            else:
                idx = bisect_left(candies, mid)
                if sum(candies[i] // mid for i in range(idx, N)) >= k:
                    lo = mid + 1
                else:
                    hi = mid - 1
        
        idx = bisect_left(candies, lo)
        if sum(candies[i] // lo for i in range(idx, N)) >= k:
            return lo
        return hi
        

sol = Solution()
tests = [
    ([5, 8, 6], 3, 5),
    ([2, 5], 11, 0),
    ([43,4,5,65,7,89,9,87,6,5,4,3], 23, 11),
    ([4,7,5], 4, 3),
    ([4, 5], 3, 2),
    ([9,10,1,2,10,9,9,10,2,2], 3, 10),
]

for i, (candies, k, ans) in enumerate(tests):
    res = sol.maximumCandies(candies, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
