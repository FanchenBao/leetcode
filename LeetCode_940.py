# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def distinctSubseqII(self, s: str) -> int:
        """I did check the hint that this problem is DP, and I also used trial
        and error to find the pattern of DP. But overall, I still considered
        this problem solved by myself, with a bit external help.

        The idea is to use dp[i] to represent the total number of unique sub-
        sequences ending in s[i]. Then for s[i + 1], if there is no occurence
        of s[i + 1] before, we simply record dp[i + 1] = (dp[i] + 1) + dp[i]

        However, if s[i + 1] occurrs before, let's say it has occurred at s[j],
        then we need to remove all potential duplicates that are the same when
        ending in the previous s[j] and the current s[i + 1]. The number of
        these duplicates is dp[j - 1], which is the total number of unique
        subsequences right before the previous s[j]. So
        dp[i + 1] = (dp[i] + 1) + dp[i] - 1 - dp[j - 1]

        And don't forget to MOD.

        O(N), 53 ms, faster than 95.00%.
        """
        dp = [0] * (len(s) + 1)
        lastseen = {}
        for i, le in enumerate(s):
            if le not in lastseen:
                dp[i + 1] = 2 * dp[i] + 1
            else:
                dp[i + 1] = 2 * dp[i] - dp[lastseen[le]]
            lastseen[le] = i
        return dp[-1] % (10**9 + 7)


class Solution2:
    def distinctSubseqII(self, s: str) -> int:
        """It is possible to solve this in O(1) space, which requires that
        we do not use a dp list. Instead, we just keep pre. In addition, we use
        the lastseen dict to record the number of potential duplicates of the
        last seen letter, instead of recording its index.

        Inspired by https://leetcode.com/problems/distinct-subsequences-ii/solution/222425

        O(1) space, O(N) time.
        """
        pre = 0
        lastseen_counts = {}
        for le in s:
            cur = 2 * pre
            cur += 1 if le not in lastseen_counts else -lastseen_counts[le]
            lastseen_counts[le] = pre
            pre = cur
        return pre % (10**9 + 7)


sol = Solution2()
tests = [
    ("abc", 7),
    ("abca", 14),
    ('abcab', 27),
    ('abcabca', 95),
    ('abcabcab', 176),
    ('abcabcabc', 325),
    ('aba', 6),
    ('aaa', 3),
    ("zchmliaqdgvwncfatcfivphddpzjkgyygueikthqzyeeiebczqbqhdytkoawkehkbizdmcnilcjjlpoeoqqoqpswtqdpvszfaksn", 97915677),
]

for i, (s, ans) in enumerate(tests):
    res = sol.distinctSubseqII(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
