# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """LeetCode 1220

        Naive DP solution.

        O(5N), 509 ms, faster than 55.24%
        """
        dp = [1, 1, 1, 1, 1]
        for _ in range(2, n + 1):
            dp = [dp[1], dp[0] + dp[2], sum(dp) - dp[2], dp[2] + dp[4], dp[0]]
        return sum(dp) % 1000000007


sol = Solution()
tests = [
    (1, 5),
    (2, 10),
    (5, 68),
]

for i, (n, ans) in enumerate(tests):
    res = sol.countVowelPermutation(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
