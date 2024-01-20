# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """
        LeetCode 931

        Use DP and BFS.

        O(N^2)
        """
        N = len(matrix)
        dp = matrix[-1]
        for i in range(N - 2, -1, -1):
            tmp = [math.inf] * N
            for j in range(N):
                if j > 0:
                    tmp[j - 1] = min(tmp[j - 1], dp[j] + matrix[i][j - 1])
                tmp[j] = min(tmp[j], dp[j] + matrix[i][j])
                if j < N - 1:
                    tmp[j + 1] = min(tmp[j + 1], dp[j] + matrix[i][j + 1])
            dp = tmp
        return min(dp)


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
