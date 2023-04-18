# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """LeetCode 1431

        26 ms, faster than 99.39%
        """
        max_candy = max(candies)
        return [(c + extraCandies) >= max_candy for c in candies]


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
