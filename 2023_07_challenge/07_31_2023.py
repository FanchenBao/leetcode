# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache
from itertools import accumulate


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """LeetCode 712

        Much simpler DP than yesterday. The only troublesome part is the edge
        case when i < 0 or j < 0. To compute them faster, I use prefix sum.

        O(MN), 830 ms, faster than 41.82%
        """
        psum1 = list(accumulate(ord(e) for e in s1))
        psum2 = list(accumulate(ord(e) for e in s2))
        
        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            """dp(i, j) returns the min ASCII sum that makes s1[:i + 1] and
            s2[:j + 1] equal
            """
            if i < 0 and j < 0:
                return 0
            if i < 0:
                return psum2[j]
            if j < 0:
                return psum1[i]
            if s1[i] == s2[j]:
                return dp(i - 1, j - 1)
            return min(dp(i - 1, j) + ord(s1[i]), dp(i, j - 1) + ord(s2[j]))

        return dp(len(s1) - 1, len(s2) - 1)


sol = Solution()
tests = [
    ('sea', 'eat', 231),
    ('delete', 'leet', 403),
]

for i, (s1, s2, ans) in enumerate(tests):
    res = sol.minimumDeleteSum(s1, s2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
