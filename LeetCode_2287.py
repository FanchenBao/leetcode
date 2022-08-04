# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter
import math


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        """O(N + M), 38 ms, faster than 78.73%
        """
        cs, ct = Counter(s), Counter(target)
        res = math.inf
        for le, count in ct.items():
            res = min(res, cs[le] // count)
        return res
        

sol = Solution()
tests = [
    ("ilovecodingonleetcode", "code", 2),
    ("abcba", "abc", 1),
]

for i, (s, target, ans) in enumerate(tests):
    res = sol.rearrangeCharacters(s, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
