# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution1:
    def numberOfSubstrings(self, s: str) -> int:
        """Use DP. dp[i] equals the number of strings that end in
        s[i] and contains only 'a', 'b', 'c', 'ab', 'ac', 'bc', and 'abc'. Then
        when we get to s[i + 1], we can use the dp[i] to compute dp[i + 1].

        To speed things up, we use an array to represent each element of dp.

        O(7N), 833 ms, faster than 19.30%
        """
        dp = [0] * 7  # [a, b, c, ab, ac, bc, abc]
        res = 0
        for le in s:
            tmp = [0] * 7
            if le == 'a':
                tmp[0] = dp[0] + 1
                tmp[3] = dp[1] + dp[3]
                tmp[4] = dp[2] + dp[4]
                tmp[6] = dp[5] + dp[6]
            elif le == 'b':
                tmp[1] = dp[1] + 1
                tmp[3] = dp[0] + dp[3]
                tmp[5] = dp[2] + dp[5]
                tmp[6] = dp[4] + dp[6]
            else:  # le == 'c'
                tmp[2] = dp[2] + 1
                tmp[5] = dp[1] + dp[5]
                tmp[4] = dp[0] + dp[4]
                tmp[6] = dp[3] + dp[6]
            dp = tmp
            res += dp[6]
        return res


class Solution2:
    def numberOfSubstrings(self, s: str) -> int:
        """Second sliding window solution from lee215

        Ref: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/discuss/516977/JavaC%2B%2BPython-Easy-and-Concise

        We find the first s[i:j + 1] that contains 'abc'. Then before we find
        the next substring that contains all 'abc', each time j expands, we have
        to add i number of substring to the result. Until we find the next
        s[m:n + 1] that contains 'abc', we repeat the same process.

        Very smart method.

        O(N) time, O(1) space, 368 ms, faster than 73.64%
        """
        last = [-1, -1, -1]  # the last occurred index of 'a', 'b', 'c'
        res = 0
        for i, le in enumerate(s):
            last[ord(le) - 97] = i
            res += 1 + min(last)  # this is sliding window
        return res



sol = Solution2()
tests = [
    ("abcabc", 10),
    ("aaacb", 3),
    ("abc", 1),
]

for i, (s, ans) in enumerate(tests):
    res = sol.numberOfSubstrings(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
