# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        """LeetCode 1232

        The edge case is when two points have the same x coord. I fell for that.

        O(N), 79 ms, faster than 30.76%
        """
        k = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0]) if coordinates[1][0] - coordinates[0][0] else math.inf
        for i in range(1, len(coordinates) - 1):
            new_k = (coordinates[i + 1][1] - coordinates[i][1]) / (coordinates[i + 1][0] - coordinates[i][0]) if coordinates[i + 1][0] - coordinates[i][0] else math.inf
            if not math.isclose(k, new_k):
                return False
        return True


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
