# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        """LeetCode 2279

        Get the difference between capacity and rocks, sort it ascending, and
        fill as many bags as possible from left to right.

        O(NlogN), 922 ms, faster than 97.37%
        """
        rem = sorted([c - r for c, r in zip(capacity, rocks)])
        res = 0
        for r in rem:
            if additionalRocks >= r:
                additionalRocks -= r
                res += 1
            else:
                break
        return res


sol = Solution()
tests = [
    ([2,3,4,5], [1,2,4,4], 2, 3),
    ([10,2,2], [2,2,0], 100, 3),
]

for i, (capacity, rocks, additionalRocks, ans) in enumerate(tests):
    res = sol.maximumBags(capacity, rocks, additionalRocks)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
