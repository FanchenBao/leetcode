# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict, Counter
from bisect import bisect_left


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        N = len(s)
        lpsum = {'a': [0], 'b': [0], 'c': [0]}
        rpsum = {'a': [0], 'b': [0], 'c': [0]}
        for i in range(N):
            for le in lpsum.keys():
                lpsum[le].append(lpsum[le][-1] + int(le == s[i]))
        for j in range(N - 1, -1, -1):
            for le in lpsum.keys():
                rpsum[le].append(rpsum[le][-1] + int(le == s[j]))
        res = math.inf
        for lt in range(len(lpsum['a'])):
            t = 0
            for le in lpsum.keys():
                lc = lpsum[le][lt]
                rt = bisect_left(rpsum[le], k - lc)
                if lt + rt > N:
                    break
                t = max(t, lt + rt)
            else:
                res = min(res, t)
        return res if res < math.inf else -1



sol = Solution()
tests = [
    ("aabaaaacaabc", 2, 8),
    ("a", 1, -1),
    ("aabaaaacaabcb", 2, 6),
    ("acba", 1, 3),
    ("cbaabccac", 3, -1),
]

for i, (s, k, ans) in enumerate(tests):
    res = sol.takeCharacters(s, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
