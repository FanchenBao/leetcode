# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def partitionString(self, s: str) -> int:
        """LeetCode 2405

        Greedy. Try to find the max substring with unique letters for each
        partition going from left to right.

        O(N), 103 ms, faster than 89.18%
        """
        seen = set()
        res = 0
        for le in s:
            if le in seen:
                res += 1
                seen.clear()
            seen.add(le)
        return res + 1
        

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
