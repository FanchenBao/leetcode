# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """LeetCode 931

        Basic DP

        O(N^2), 392 ms, faster than 24.77% 
        """
        N = len(matrix)
        for i in range(1, N):
            for j in range(N):
                matrix[i][j] += min(matrix[i - 1][max(j - 1, 0):min(j + 2, N)])
        return min(matrix[-1])
        

sol = Solution()
tests = [
    ([[2,1,3],[6,5,4],[7,8,9]], 13),
    ([[-19,57],[-40,-5]], -59)
]

for i, (matrix, ans) in enumerate(tests):
    res = sol.minFallingPathSum(matrix)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
