# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        LeetCode 907

        Use monotonic increasing stack.
        O(N)
        """
        MOD = 1000000007
        res = 0
        stack = []
        dp = [0] * len(arr)
        for i, a in enumerate(arr):
            while stack and arr[stack[-1]] >= a:
                stack.pop()
            if stack:
                dp[i] += (dp[stack[-1]] + a * (i - stack[-1])) % MOD
            else:
                dp[i] += (a * (i + 1)) % MOD
            stack.append(i)
            res = (res + dp[i]) % MOD
        return res


sol = Solution()
tests = [
    ([3,1,2,4], 17),
    ([11,81,94,43,3], 444),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.sumSubarrayMins(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
