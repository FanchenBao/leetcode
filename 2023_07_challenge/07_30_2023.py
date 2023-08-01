# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import groupby
from functools import lru_cache


class Solution1:
    def strangePrinter(self, s: str) -> int:
        """LeetCode 664

        Probably one of the most difficult DP I have encountered. This is the
        same solution as the official solution, but implemented via lru_cache.

        dp(l, r) is the number of prints to fix sequence of (r - l + 1) number
        of s[r] into the correct s[l:r + 1]. But I don't quite like this way
        of thinking. So let's turn to Solution2.

        1252 ms, faster than 40.00%
        """
        
        @lru_cache(maxsize=None)
        def dp(l: int, r: int) -> int:
            if l == r:
                return 0
            res = math.inf
            for j in range(l, r):
                if s[j] != s[r]:
                    for i in range(j, r):
                        res = min(res, 1 + dp(j, i) + dp(i + 1, r))
                    break
            return res if res < math.inf else 0

        return dp(0, len(s) - 1) + 1


class Solution2:
    def strangePrinter(self, s: str) -> int:
        """This is inspired by https://leetcode.com/problems/strange-printer/discuss/118769/Proof-of-O(n3)-algorithms

        For each letter in s, there might be some print starting from that
        letter. If that is the case, that starting letter will not change once
        printed. Thus, we can say dp(l, r) is the number of prints to change
        r - l + 1 number of s[l] into the correct final version.

        Now that we are dealing with dp(l, r). There are two scenarios. First,
        we print s[l], then handle the remaining dp(l + 1, r) from scratch.

        Second, we go through l + 1 to r and find s[k] == s[l]. When that
        happens, the amount of prints to make s[l:k + 1] correct is equivalent
        to dp(l, k - 1), because when we do dp(l, k - 1) we print s[l] all the
        way to k - 1. We might as well extend that by one more position, and
        all the other changes needed in dp(l, k - 1) can be identically applied
        to king s[l:k + 1] work. Once s[l:k + 1] are done, we deal with s[k + 1:
        r] using dp(k + 1, r).

        Another trick is to remove all the consecutivly identical letters,
        because they can all be printed in one run.

        O(N^3), 213 ms, faster than 92.62%
        """
        ss = [k for k, _ in groupby(s)]

        @lru_cache(maxsize=None)
        def dp(l: int, r: int) -> int:
            if l > r:
                return 0
            res = 1 + dp(l + 1, r)  # First scenario
            for k in range(l + 1, r + 1):
                if ss[l] == ss[k]:  # Second secario for all ss[l] == ss[k]
                    res = min(res, dp(l, k - 1) + dp(k + 1, r))
            return res

        return dp(0, len(ss) - 1)



sol = Solution2()
tests = [
    ('aaabbb', 2),
    ('aba', 2),
    ('sdsdsds', 4),
    ("abcabc", 5),
    ("oifofi", 4),
    ("baacdddaaddaaaaccbddbcabdaabdbbcdcbbbacbddcabcaaa", 19),
]

for i, (s, ans) in enumerate(tests):
    res = sol.strangePrinter(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
