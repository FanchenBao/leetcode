# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """LeetCode 1207

        O(N), 34 ms, faster than 96.76% 
        """
        c = Counter(arr)
        return len(set(list(c.values()))) == len(c)


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
