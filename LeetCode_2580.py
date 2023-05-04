# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        """Find the total count of non-overlapping ranges. Suppose there are n
        of them, then the answer is

        0Cn + 1Cn + 2Cn + ... + nCn = 2^n

        O(N), 912 ms, faster than 59.18%
        """
        ranges.sort()
        non_overlapping_count = 0
        pr = -1
        for l, r in ranges:
            if l > pr:
                non_overlapping_count += 1
            pr = max(pr ,r)
        return 2**non_overlapping_count % (10**9 + 7)


sol = Solution()
tests = [
    ([[6,10],[5,15]], 2),
    ([[1,3],[10,20],[2,5],[4,8]], 4),
    ([[1,2],[3,4],[5,6],[7,8],[9,10]], 32),
]

for i, (ranges, ans) in enumerate(tests):
    res = sol.countWays(ranges)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
