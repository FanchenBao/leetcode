# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def longestPalindrome(self, s: str) -> str:
        """LeetCode 5

        Keep a DP list of all the lengths of palindrome ending at the letter
        to the left of the current letter, and produce a new DP list recording
        all the palindrome lengths ending at the current letter.

        O(N^2), 2303 ms, faster than 26.72%
        """
        dp = [1]
        res = (1, 0)
        for i in range(1, len(s)):
            temp = [1]
            if s[i] == s[i - 1]:
                temp.append(2)
            for pl in dp:
                if i - 1 - pl >= 0 and s[i - 1 - pl] == s[i]:
                    temp.append(pl + 2)
            if max(temp) > res[0]:
                res = (max(temp), i)
            dp = temp
        return s[res[1] + 1 - res[0]:res[1] + 1]


class Solution2:
    def longestPalindrome(self, s: str) -> str:
        """Manacher's algorithm. It's not trivial and quite tricky for me.

        O(N), 289 ms, faster than 94.34%
        """
        s_ = '#'.join('^' + s + '&')
        dp = [0] * len(s_)
        c, r = 0, 0
        for i in range(1, len(s_) - 1):
            if i > c + r:
                dp[i] = 0
            else:
                # dp[2 * c - i] is the situation where the palindrome centered
                # on i does not extend beyond c + r
                # c + r - i is the situation where the palindrome centered on i
                # extends beyond c + r
                dp[i] = min(dp[2 * c - i], c + r - i)
            while s_[i + dp[i]] == s_[i - dp[i]]:
                dp[i] += 1
            dp[i] -= 1
            if c + r < i + dp[i]:
                c, r = i, dp[i]
        idx, max_d = 0, 0
        for i, d in enumerate(dp):
            if d > max_d:
                idx = i
                max_d = d
        return s[(idx - max_d - 1) // 2:(idx + max_d -1) // 2]



sol = Solution2()
tests = [
    ("babad", "bab"),
    ("cbbd", "bb"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.longestPalindrome(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
