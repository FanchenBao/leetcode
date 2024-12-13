# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import groupby


class Solution:
    def maximumLength(self, s: str) -> int:
        """
        One pass solution. Find the top three length of the substring of the
        same letter. Then analyze different situations of the size comparison
        among the top three.

        O(N), 222 ms, faster than 94.96%
        """
        top_three = [[0] * 3 for _ in range(26)]
        for k, g in groupby(s):
            size = len(list(g))
            i = ord(k) - 97
            if size > top_three[i][0]:
                top_three[i][0], top_three[i][1], top_three[i][2] = (
                    size,
                    top_three[i][0],
                    top_three[i][1],
                )
            elif size > top_three[i][1]:
                top_three[i][1], top_three[i][2] = size, top_three[i][1]
            elif size > top_three[i][2]:
                top_three[i][2] = size
        res = 0
        for t0, t1, t2 in top_three:
            cur_max = t1
            if t0 == t2:
                cur_max = t0
            elif t0 == t1:
                cur_max = t0 - 1
            elif t0 - 2 > t1:
                cur_max = t0 - 2
            res = max(res, cur_max)
        return res if res > 0 else -1


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
