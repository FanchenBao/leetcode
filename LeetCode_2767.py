# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution1:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        """
        Since s has max length of 15, this means there are only seven different
        possible power of five that are within the range for s. Therefore, we
        can try these seven power of fives one by one for the string. If we have
        a match, we divide the string into two additional substrings, which will
        undergo the same process as before. We keep track of the smallest number
        of substrings throughout the entire process.

        We use memoization to reduce the amount of computation.

        O(N^3 * 7), 50 ms, faster than 71.60%
        """
        bases = [
            '1',
            '101',
            '11001',
            '1111101',
            '1001110001',
            '110000110101',
            '11110100001001',
        ]

        @lru_cache(maxsize=None)
        def helper(substr: str) -> int:
            if not substr:
                return 0
            res = math.inf
            for b in bases:
                idx = substr.find(b)
                if idx >= 0:
                    left = substr[:idx]
                    right = substr[idx + len(b):]
                    res = min(res, 1 + helper(left) + helper(right))
            return res

        res = helper(s)
        return res if res < math.inf else -1


class Solution2:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        """
        Inspired by lee215
        https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/discuss/3737219/JavaC%2B%2BPython-DP

        Still DP, but dp[i] is the min number of partitions to create substrings
        for s[:i + 1]

        Also, a faster way to identify whether a binary number is power of 5 is
        to test whether it is divisible by 5^6 = 15625
        
        O(N^2), 44 ms, faster than 83.95%
        """
        dp = [math.inf] * len(s)
        DIV = 15625
        for i in range(len(s)):
            cur = 0
            for j in range(i, -1, -1):
                if s[j] == '0':
                    continue
                cur += int(s[j]) << (i - j)
                if cur > DIV:
                    break
                if DIV % cur == 0:
                    dp[i] = min(dp[i], (dp[j - 1] + 1) if j >= 1 else 1)
        return dp[-1] if dp[-1] < math.inf else -1


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
