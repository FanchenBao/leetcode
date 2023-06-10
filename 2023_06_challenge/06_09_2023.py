# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_right


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """LeetCode 744

        Binary search.

        136 ms, faster than 44.01%
        """
        idx = bisect_right(letters, target)
        return letters[idx % len(letters)]
        

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
