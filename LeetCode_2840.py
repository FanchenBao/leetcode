# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution1:
    def checkStrings(self, s1: str, s2: str) -> bool:
        """
        Ensure that the composition of all the letters at
        the even and odd positions are the identical.

        O(NlogN) 143 ms, faster than 73.74%
        """
        N = len(s1)
        e1 = [s1[i] for i in range(0, N, 2)]
        e2 = [s2[i] for i in range(0, N, 2)]
        if sorted(e1) != sorted(e2):
            return False
        o1 = [s1[i] for i in range(1, N, 2)]
        o2 = [s2[i] for i in range(1, N, 2)]
        return sorted(o1) == sorted(o2)


class Solution2:
    def checkStrings(self, s1: str, s2: str) -> bool:
        """
        Forgot how to write succinct Python using all its syntax sugar

        90 ms, faster than 94.44%
        """
        return Counter(s1[::2]) == Counter(s2[::2]) and Counter(s1[1::2]) == Counter(
            s2[1::2]
        )


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
