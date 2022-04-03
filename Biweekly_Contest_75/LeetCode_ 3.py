# from pudb import set_trace; set_trace()
from typing import List
from itertools import groupby
from collections import defaultdict


class Solution:
    def numberOfWays(self, s: str) -> int:
        res = 0
        presum = [0, 0]
        if s[0] == '0':
            s0, s1 = 1, 0
        else:
            s0, s1 = 0, 1
        for i in range(1, len(s)):
            if s[i] == '0':
                s0 += 1
                if s[i] != s[i - 1]:
                    presum.append(s1 + presum[-2])
                    s1 = 0
            else:
                s1 += 1
                if s[i] != s[i - 1]:
                    presum.append(s0 + presum[-2])
                    s0 = 0
        if s0:
            presum.append(s0 + presum[-2])
        else:
            presum.append(s1 + presum[-2])
        N = len(presum)
        if (N - 1) % 2:
            last_even_idx = N - 2
            last_odd_idx = N - 1
        else:
            last_even_idx = N - 1
            last_odd_idx = N - 2
        for i in range(2, N - 2):
            for j in range(i + 1, N, 2):
                res += (presum[i] - presum[i - 2]) * (presum[j] - presum[j - 2]) * ((presum[last_odd_idx] - presum[j - 1]) if i % 2 else (presum[last_even_idx] - presum[j - 1]))
        return res

                
sol = Solution()
tests = [
    ('001101', 6),
    ('111000', 0),
    ("0001100100", 38),
]

for i, (s, ans) in enumerate(tests):
    res = sol.numberOfWays(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
