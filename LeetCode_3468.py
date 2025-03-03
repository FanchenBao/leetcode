# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        """
        Starting from the first bound and move forward. Use the original to
        find the diff so that we can compute the expected bound of the next
        bound. Compare the expected bound with the actual bound and find their
        intersection to be the new eligible bound.

        Whenever the eligible bound is impossible (i.e., hi < lo), we return
        0. Otherwise, we keep going until all the bounds are considered.
        The answer is the number of values in the final bound.

        O(N), 68 ms, 50%
        """
        lo, hi = bounds[0][0], bounds[0][1]
        for i in range(1, len(bounds)):
            diff = original[i] - original[i - 1]
            clo, chi = max(lo + diff, bounds[i][0]), min(hi + diff, bounds[i][1])
            if chi < clo:
                return 0
            lo, hi = clo, chi
        return hi - lo + 1


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
