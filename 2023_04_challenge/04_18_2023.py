# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """LeetCode 1768

        Similar logic to merge sort.

        O(N + M), 24 ms, faster than 96.72%
        """
        i = j = 0
        res = ''
        M, N = len(word1), len(word2)
        while i < M and j < N:
            if i == j:
                res += word1[i]
                i += 1
            else:
                res += word2[j]
                j += 1
        if i < M:
            res += word1[i:]
        if j < N:
            res += word2[j:]
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
