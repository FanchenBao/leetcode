# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def longestPalindrome(self, s: str) -> str:
        """We identify the center of each potential palindrome and expand from
        there. We record the indices of the start and end of each palindrome
        that is larger than the last. Eventually we can return the largest.

        UPDATE: surprisingly, this is one of the official solutions.

        O(N^2), 1348 ms, 43% ranking
        """
        res = [0, 0]
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                m, n = i - 1, i
                while m >= 0 and n < len(s) and s[m] == s[n]:
                    if n - m > res[1] - res[0]:
                        res[0], res[1] = m, n
                    m -= 1
                    n += 1
            if i >= 2 and s[i] == s[i - 2]:
                m, n = i - 2, i
                while m >= 0 and n < len(s) and s[m] == s[n]:
                    if n - m > res[1] - res[0]:
                        res[0], res[1] = m, n
                    m -= 1
                    n += 1
        return s[res[0]:res[1] + 1]


class Solution2:
    def longestPalindrome(self, s: str) -> str:
        """My attempt at Manacher's algorithm

        O(N), 168 ms, 94% ranking
        """
        padded_s = '#' + '#'.join(list(s)) + '#'
        # P[i] records the max right reach of palindrome centered at i
        P = [0] * len(padded_s)
        P[1] = 1
        C = 1  # P[C] has the max right reach uptil the current i
        res_idx = 1
        for i in range(2, len(padded_s)):
            R = C + P[C]  # the max right reach
            j = 2 * C - i  # the mirror of i centered around C
            # mirror palindrome of j, when applied to i, does not exceed C's
            # right reach
            if P[j] + i < R:
                P[i] = P[j]
            else:
                # the mirrored letters right outside of the max right reach
                l, r = 2 * i - R - 1 , R + 1
                while l >= 0 and r < len(padded_s) and padded_s[l] == padded_s[r]:
                    l -= 1
                    r += 1
                P[i] = r - i - 1
            if i + P[i] > R:  # update C when current i has more right reach
                C = i
            res_idx = i if P[i] > P[res_idx] else res_idx
        # Find the substring in the original s
        res_c, res_len = res_idx // 2, P[res_idx]
        return s[res_c - res_len // 2:res_c + res_len // 2 + res_len % 2]


class Solution3:
    def longestPalindrome(self, s: str) -> str:
        """Manacher's algorithm with better implementation.

        https://leetcode.com/problems/longest-palindromic-substring/discuss/3337/Manacher-algorithm-in-Python-O(n)

        O(N), 144 ms, 95% ranking
        """
        # Use different front and end padding such that no boundary check
        # is needed when expanding from i outwards. e.g 'babad' =>
        # '^#b#a#b#a#d&'
        padded_s = '#'.join(f'^{s}&')
        # P[i] records the max right reach of palindrome centered at i
        P = [0] * len(padded_s)
        C = R = 0  # center and max right reach
        # range does not include extra front and end
        for i in range(1, len(padded_s) - 1):
            # default P[i] value, either 0 or the smaller of the two scenario:
            # mirror j's reach when this reach is smaller than R, or the
            # distance between i to R when mirror j's reach exceeds R.
            P[i] = (R > i) and min(P[2 * C - i], R - i)
            while padded_s[i + P[i] + 1] == padded_s[i - P[i] - 1]:
                P[i] += 1
            if i + P[i] > R:
                C, R = i, i + P[i]
        # Find the substring in the original s
        res_len, res_c = max((p, idx) for idx, p in enumerate(P))
        return s[(res_c - res_len) // 2:(res_c + res_len) // 2]


sol = Solution3()
tests = [
    ('babad', 'bab'),
    ('cbbd', 'bb'),
    ('a', 'a'),
    ('ac', 'a'),
]

for i, (s, ans) in enumerate(tests):
    res = sol.longestPalindrome(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
