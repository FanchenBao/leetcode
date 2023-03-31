# from pudb import set_trace; set_trace()
from typing import List, Set
import math
from functools import lru_cache
from collections import Counter


class Solution1:
    def isScramble(self, s1: str, s2: str) -> bool:
        """LeetCode 87

        This is the 1000th day!!

        We use helper function to check whether s1[l1:h1 + 1] is a scramble of
        s2[l2:h2 + 1].

        To make the check, we get s1[l1:l1 + k] and compare it to s2[l2:l2 + k]
        or s2[h2 + 1 - k:h2 + 1]. If either one matches in terms of components
        of the letters, we know that might be a correct partition. We continue
        down that path. If no match, we terminate that path.

        142 ms, faster than 30.56%
        """
        if Counter(s1) != Counter(s2):
            return False

        N = len(s1)

        @lru_cache(maxsize=None)
        def helper(l1: int, h1: int, l2: int, h2: int) -> bool:
            if l1 == h1 and l2 == h2:
                return s1[l1] == s2[l2]
            c1, c2lr, c2rl = Counter(), Counter(), Counter()
            res = False
            for i in range(l1, h1):
                c1[s1[i]] += 1
                c2lr[s2[l2 + i - l1]] += 1
                c2rl[s2[h2 - i + l1]] += 1
                if c1 == c2lr:
                    res |= (helper(l1, i, l2, l2 + i - l1) and helper(i + 1, h1, l2 + i - l1 + 1, h2))
                if c1 == c2rl:
                    res |= (helper(l1, i, h2 - i + l1, h2)) and (helper(i + 1, h1, l2, h2 - i + l1 - 1))
            return res            


        return helper(0, N - 1, 0, N - 1)


class Solution2:
    @lru_cache(maxsize=None)
    def isScramble(self, s1: str, s2: str) -> bool:
        """This was the solution I submitted last time, more than three years
        ago, most likely from the official solution.

        Instead of playing with indices, we can use substring directly in the
        recursion.

        Don't forget to memoize it!

        O(N^4), 83 ms, faster than 41.20%

        It's O(N^4) because there are N^2 number of substrings in s1 and s2.
        We cross each pair of them, which results in N^4 total possible pairings
        during recursion.
        """
        if Counter(s1) != Counter(s2):
            return False

        if s1 == s2:
            return True

        for k in range(1, len(s1)):
            if (
                self.isScramble(s1[:k], s2[:k]) and
                self.isScramble(s1[k:], s2[k:])
            ) or  (
                self.isScramble(s1[:k], s2[-k:]) and
                self.isScramble(s1[k:], s2[:-k])
            ):
                return True
        return False


sol = Solution2()
tests = [
    ("great", "rgeat", True),
    ("abcde", "caebd", False),
    ("a", "a", True),
]

for i, (s1, s2, ans) in enumerate(tests):
    res = sol.isScramble(s1, s2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
