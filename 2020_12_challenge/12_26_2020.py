# from pudb import set_trace; set_trace()
from typing import List



class Solution1:
    def numDecodings(self, s: str) -> int:
        """DP. For position i in s, the number of ways to decode can be split
        into two situations. One, s[i] decodes by itself, then the number of
        ways to decode is the same as the number of ways to decode s[:i]
        multiplied by the number of ways to decode s[i]. Two,
        s[i - 1:i + 1] decode together, then the number of ways to decode is
        the same as the number of ways to decode s[:i - 1] multiplied by
        the number of ways to decode s[i - 1;i + 1]. We use a 1d array to store
        the results of the number of ways to decode s[:i] for each i.

        O(N), 36 ms, 27% ranking
        """
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        ways = {str(i): 1 for i in range(1, 27)}
        for i in range(len(s)):
            dp[i + 1] = dp[i] * ways.get(s[i], 0)
            if i > 0:
                dp[i + 1] += dp[i - 1] * ways.get(s[i - 1:i + 1], 0)
        return dp[-1]


class Solution2:
    def numDecodings(self, s: str) -> int:
        """Same DP, but smarter. Referring to Mr. Pochmann

        pre_le: Previous letter
        pre_w: Number of ways to decode the string ending with pre_le
        cur_w: Number of ways to decode the string ending with the current
            letter.

        O(N), 32 ms, 63% ranking.
        """
        pre_le, pre_w, cur_w = '', 1, 1
        for d in s:
            pre_le, pre_w, cur_w = d, cur_w, cur_w * (d != '0') + pre_w * (10 <= int(pre_le + d) <= 26)
        return cur_w


sol = Solution2()
tests = [
    ('12', 2),
    ('226', 3),
    ('0', 0),
    ('1', 1),
    ('1203312', 2),
    ('123312', 6),
    ('10011', 0),
]

for i, (s, ans) in enumerate(tests):
    res = sol.numDecodings(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
