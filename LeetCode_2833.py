# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        """
        Pick the L or R with larger frequency, and convert the
        underscore to that move.
        """
        counter = Counter(moves)
        return len(moves) - 2 * min(counter["L"], counter["R"])


# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]
#
# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
