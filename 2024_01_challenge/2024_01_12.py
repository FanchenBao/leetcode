# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        """
        LeetCode 1704

        Count the vowels on the left and right

        O(N), 37 ms, faster than 83.40%
        """
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        lc = rc = 0
        for i in range(len(s) // 2):
            lc += s[i] in vowels
        for i in range(len(s) // 2, len(s)):
            rc += s[i] in vowels
        return lc == rc


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
