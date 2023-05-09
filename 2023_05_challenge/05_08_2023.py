# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        """LeetCode 1572
        
        O(N), 127 ms, faster than 5.85%
        """
        N = len(mat)
        res = 0
        for i in range(N):
            res += mat[i][i]
            res += mat[i][N - 1 - i]
        if N % 2:
            res -= mat[N // 2][N // 2]
        return res
        

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
