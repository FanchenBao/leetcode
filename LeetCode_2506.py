# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter
from math import 


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        """One liner abomination.

        159 ms, faster than 58.50%
        """
        return sum(math.comb(v, 2) for v in Counter(tuple(sorted(set(word))) for word in words).values())
        

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
