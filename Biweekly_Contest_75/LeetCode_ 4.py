# from pudb import set_trace; set_trace()
from typing import List
from itertools import accumulate


class Solution:
    def sumScores(self, s: str) -> int:
        N = len(s)
        lsp = [0] * N
        # Build lsp
        pre_len = 0
        i = 1
        while i < N:
            if s[pre_len] == s[i]:
                pre_len += 1
                lsp[i] = pre_len
                i += 1
            elif pre_len != 0:
                pre_len = lsp[pre_len - 1]
            else:
                lsp[i] = 0
                i += 1
        print(lsp)
        dp = [0] * N
        dp[0] = N
        for i in range(1, N):
            if lsp[i] > 0:
                dp[i - lsp[i] + 1] = max(dp[i - lsp[i] + 1], lsp[i])
        return sum(dp)


sol = Solution()
tests = [
    ('babab', 9),
    # ('azbazbzaz', 14),
]

for i, (s, ans) in enumerate(tests):
    res = sol.sumScores(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
