# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """I wasn't able to solve this yesterday (got tons of TLE). And I knew
        that the solution yesterday was bad, because the logic was very
        convoluted. Today, I still couldn't crack it, so I took a look at
        "Similar Questions" and noticed that LCS was there. Thus, I started to
        think in terms of LCS. Palindrome is similar to LCS in the sense that
        we are trying to find the common subsequence from the front and from
        the back. Thus, I had the idea of putting the two pointers one at the
        beginning and one at the back, and then move them inwards. The logic
        is the same as LCS. If s[lo] == s[hi], then these two letters must be
        involved in the longest palindrome. Then we move both pointers. If
        s[lo] != s[hi], then we do the cross calling of (lo + 1, hi) and
        (lo, hi - 1). That's it.

        O(N^2), 1245 ms, 88% ranking.
        """
        
        @lru_cache(maxsize=None)
        def helper(lo: int, hi: int) -> int:
            if lo == hi:
                return 1
            if lo > hi:
                return 0
            if s[lo] == s[hi]:
                return 2 + helper(lo + 1, hi - 1)
            return max(helper(lo + 1, hi), helper(lo, hi - 1))

        return helper(0, len(s) - 1)

        
sol = Solution()
tests = [
    ('bbbab', 4),
    ('cbbd', 2),
    ("gsgrnhdgf", 3),
]

for i, (s, ans) in enumerate(tests):
    res = sol.longestPalindromeSubseq(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
