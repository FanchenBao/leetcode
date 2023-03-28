# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import accumulate


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """LeetCode 64

        DP. O(MN), 97 ms, faster than 77.56%
        """
        M, N = len(grid), len(grid[0])
        dp = list(accumulate(grid[0]))
        for i in range(1, M):
            for j in range(N):
                if j == 0:
                    dp[j] += grid[i][j]
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        return dp[-1]



# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
