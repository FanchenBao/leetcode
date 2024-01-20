# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import chain


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        """
        Note that we have to check whether the string is empty and not include
        it in the solution.
        """
        return [s for s in (chain(*[w.split(separator) for w in words])) if s]


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
