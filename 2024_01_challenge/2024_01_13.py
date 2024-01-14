# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter
from string import ascii_lowercase


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        """
        LeetCode 1347

        The only letters allowed to change is the extra ones in t that do not
        exist in s. Thus, the problem is equivalent to counting the number of
        extra letters in t.

        O(N), 100 ms, faster than 92.50% 
        """
        sc = Counter(s)
        tc = Counter(t)
        res = 0
        for c in ascii_lowercase:
            res += max(0, tc[c] - sc[c])
        return res



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
