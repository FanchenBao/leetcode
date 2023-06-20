# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        """ 936 ms, faster than 66.68%
        """
        res = [0, 0]
        for i, row in enumerate(mat):
            c = row.count(1)
            if c > res[1]:
                res = [i, c]
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
