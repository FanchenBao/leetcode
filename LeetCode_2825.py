# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        """
        Greedily matching the first letter in str1 that satisfies
        str2.

        O(N), 89 ms, faster than 98.21%
        """
        if len(str1) < len(str2):
            return False
        i = 0
        for c in str1:
            if c == str2[i] or (ord(c) + 1 - 97) % 26 == ord(str2[i]) - 97:
                i += 1
                if i == len(str2):
                    return True
        return False


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
