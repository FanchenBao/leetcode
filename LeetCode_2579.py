# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def coloredCells(self, n: int) -> int:
        """We can prove that given n minutes, the shape has four rugged edges,
        with n cells on the edge.

        Among these n edges, the next minute will create n - 1 new cells. Thus
        the total number of cells created in the next minute from the edges are
        4 * (n - 1).

        In addition, the four cells sticking out can produce four more cells.

        Thus the total new cells added is 4 * (n - 1) + 4 = 4 * n

        This means from the nth minute to the n + 1 th minute, we add 4 * n more
        cells.

        Thus, the total number of cells after n minutes are:

        1 + 4 + 2 * 4 + 3 * 4 + ... + (n - 1) * 4

        O(1), 43 ms, faster than 48.02%
        """
        return 1 + 2 * n * (n - 1)


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
