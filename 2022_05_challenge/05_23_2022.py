# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache
from collections import Counter


class Solution1:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """LeetCode 474

        I solved this essentially, but I forgot the "@" in front of the
        decorator, which led to TLE. I checked the solution and it was
        identical to this one, which made the whole thing even weirder. I was
        massively confused as why this solution didn't work. It took me quite
        a while to realize that there was a syntax error in the code. Facepalm

        O(KMN), where K = len(strs). 3005 ms, faster than 84.74%
        """
        cs = [Counter(s) for s in strs]

        @lru_cache(maxsize=None)
        def helper(p: int, q: int, idx: int) -> int:
            if idx < 0:
                return 0
            not_include = helper(p, q, idx - 1)
            include = 0
            if p >= cs[idx]['0'] and q >= cs[idx]['1']:
                include = 1 + helper(p - cs[idx]['0'], q - cs[idx]['1'], idx - 1)
            return max(include, not_include)

        return helper(m, n, len(cs) - 1)
        

class Solution2:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """Bottom up with efficient space complexity.
        """
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i, s in enumerate(strs, start=1):
            ones, zeros = s.count('1'), s.count('0')
            for p in range(m, -1, -1):
                for q in range(n, -1, -1):
                    if p >= zeros and q >= ones:
                        dp[p][q] = max(dp[p][q], dp[p - zeros][q - ones] + 1)
        return dp[m][n]


sol = Solution2()
tests = [
    (["10","0001","111001","1","0"], 5, 3, 4),
    (["10","0","1"], 1, 1, 2),
    (["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"],9,80,17),
]

for i, (strs, m, n, ans) in enumerate(tests):
    res = sol.findMaxForm(strs, m, n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
