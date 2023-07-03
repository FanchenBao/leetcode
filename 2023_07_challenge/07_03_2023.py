# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        """LeetCode 859

        Many situations to consider.

        1. s and goal have different length.
        2. s and goal are same
            2.1. there are repeats in s
            2.2. there is no repeat in s
        3. s and goal are not the same
            3.1. there are two mismatches
                3.1.1. the two mismatches can be corrected by swap
                3.1.2. the two mismatches cannot be corrected by swap
            3.2. there are more than or less than two mismatchs

        O(N), 57 ms, faster than 21.22%
        """
        if len(s) != len(goal):
            return False
        if s == goal:
            return max(Counter(s).values()) >= 2
        mismatch = [i for i, (a, b) in enumerate(zip(s, goal)) if a != b]
        if len(mismatch) != 2:
            return False
        return s[mismatch[0]] == goal[mismatch[1]] and s[mismatch[1]] == goal[mismatch[0]]


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
