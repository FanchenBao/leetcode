# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        """
        61 ms, faster than 14.63%
        """
        return "".join(w[0] for w in words) == s


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
