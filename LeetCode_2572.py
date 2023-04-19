# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution:
    def factor(self, n: int, primes: List[int]) -> int:
        res = 0
        i = 0
        while n > 1:
            while n % primes[i] == 0:
                if res & (1 << i):
                    return -1
                res |= (1 << i)
                n //= primes[i]
            i += 1
        return res

    def squareFreeSubsets(self, nums: List[int]) -> int:
        """The most important trick is the bit mask. But to get there does
        require some ingenuity. All I can say is I was having trouble getting
        dp to work, because it is difficult to figure out the state. The state
        shall be the product of some numbers. And since the product contains
        only singular prime factors, and the total number of prime factors is
        only 10, these are the hints for bitmask.

        Once bitmask is acquired, the DP is not that hard (but the hint of the
        problem is somewhat misleading).

        O(1024N), 972 ms, faster than 36.58%
        """
        MOD = 10**9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        reprs = []
        for n in nums:
            bitmask = self.factor(n, primes)
            if bitmask >= 0:
                reprs.append(bitmask)
        
        dp = [0] * 1024
        res = 0
        for i, rep in enumerate(reprs):
            for mask in range(len(dp)):
                if not mask & rep:
                    dp[mask | rep] = (dp[mask | rep] + dp[mask]) % MOD
            dp[rep] += 1
        return sum(dp) % MOD


sol = Solution()
tests = [
    ([3,4,4,5], 3),
    ([1], 1),
    ([5,6,4,3,4], 5),
    ([5,6,4,3,4,5,6,7,7,8,9,10,11,12,12,12,12,30,30,6,5,6,5], 203),
    ([5,6,4,3,4,5,6,7,7], 35),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.squareFreeSubsets(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
