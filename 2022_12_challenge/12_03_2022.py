# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        """LeetCode 451

        78 ms, faster than 67.50% 
        """
        return ''.join(kk * vv for vv, kk in sorted(((v, k) for k, v in Counter(s).items()), reverse=True))


sol = Solution()
tests = [
    ("tree", "eert"),
    ("cccaaa", "aaaccc"),
    ("Aabb", "bbAa"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.frequencySort(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
