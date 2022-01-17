# from pudb import set_trace; set_trace()
from typing import List
from itertools import zip_longest

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """LeetCode 290

        Such an easy problem but I stuggled mightily. The problem is with the
        many edge cases.
        """
        d1, d2 = {}, {}
        for p, w in zip_longest(list(pattern), s.split()):
            if not p or not w:
                return False
            if p not in d1:
                d1[p] = w
            if w not in d2:
                d2[w] = p
            if d1[p] != w or d2[w] != p:
                return False
        return True


sol = Solution()
tests = [
    ("aaa", "aa aa aa bb", False),
]

for i, (pattern, s, ans) in enumerate(tests):
    res = sol.wordPattern(pattern, s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
