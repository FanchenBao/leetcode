# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution1:
    def numDecodings(self, s: str) -> int:
        """LeetCode 91

        Pretty standard DP. We compute the total number of decodings from some
        idx towards the end and cache it. For any given idx, we add together
        the two possiblities: dp(idx + 1) + dp(idx + 2). The condition here is
        that s[idx] != '0' and s[idx:idx + 2] must be between 1 and 26.

        I got a little bit bogged down by the anchor case. I have four in this
        case, covering all possible ending conditions.


        O(N), 63 ms, faster than 32.28%
        """
        
        @lru_cache(maxsize=None)
        def dfs(idx: int) -> int:
            if idx >= len(s):
                return 0
            if s[idx] == '0':
                return 0
            if idx == len(s) - 1:
                return 1
            if idx == len(s) - 2:
                return dfs(idx + 1) + int(int(s[idx:idx + 2]) <= 26)
            return dfs(idx + 1) + dfs(idx + 2) * int(int(s[idx:idx + 2]) <= 26)

        return dfs(0)


class Solution2:
    def numDecodings(self, s: str) -> int:
        """This is a different way of doing DP, where we consider that
        the number of decodings in s[:i - 1] (call it p) and s[:i - 2] (call it pp)
        have been solved. Now we are at s[i], how do we proceed. We proceed
        by checking whether s[i - 1:i + 1] is within range. If it is, we add pp.
        Then we check whether s[i] is '0'. If it is not, we add p.
        """
        pp, p = 0, int(s[0] != '0')
        for i in range(1, len(s)):
            cur = int('10' <= s[i - 1:i + 1] <= '26') * (1 if i == 1 else pp)
            cur += int(s[i] != '0') * p
            pp, p = p, cur
        return p


sol = Solution2()
tests = [
    ('12', 2),
    ('226', 3),
    ('06', 0),
    ('11106', 2),
]

for i, (s, ans) in enumerate(tests):
    res = sol.numDecodings(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
