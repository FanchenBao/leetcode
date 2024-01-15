# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        LeetCode 1657

        Dict's keys can be compared directly. We only need to make sure that
        the two words are of the same length, contain the same set of letters
        and have the same occurrences of counts.
        
        NOTE: we could've used one line to solve this problem because the check
        on sorted values already contains the check on the total length.
        However, it is more costly to do so compared to directly checking the
        two strings' lengths.

        O(N), 122 ms, faster than 87.36%
        """
        if len(word1) != len(word2):
            return False
        c1, c2 = Counter(word1), Counter(word2)
        return c1.keys() == c2.keys() and sorted(c1.values()) == sorted(c2.values())


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
