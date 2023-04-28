# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        """One trick: keep modding the value converted from word. Otherwise, we
        will TLE.

        557 ms, faster than 64.24%

        UPDATE: no need to mod val again. It is already the mod of m
        """
        val = 0
        res = []
        for d in word:
            val = (val * 10 + int(d)) % m
            res.append(int(val == 0))
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
