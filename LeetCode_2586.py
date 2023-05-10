# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        """
        O(5N), 92 ms, faster than 5.27%
        """
        return sum(words[i][0] in 'aeiou' and words[i][-1] in 'aeiou' for i in range(left, right + 1))

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
