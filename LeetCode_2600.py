# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        """58 ms, faster than 5.49%
        """
        if numOnes >= k:
            return k
        if numOnes + numZeros >= k:
            return numOnes
        return numOnes - (k - numOnes - numZeros)


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
