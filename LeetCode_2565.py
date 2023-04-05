# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict, deque


class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        """Binary search.

        Produce two arrays l2r and r2l. l2r records the left-most matching index
        of s to t at each index of t going from left to right.

        r2l records the right-most matching index of s to t at each index of t
        going from right to left.

        The important observation is that the score is equal to the length of
        the substring bounded by the left most and right most removed letter.
        After the removal, the remaining t is a subsequence of s. Thus, if we
        remove the entire substring bounded by the left and right most removed
        letter, the remaining shall also be a subsequence of s. Therefore, we
        just need to find the smallest substring in t to remove such that the
        remaining is a subsequence of s.

        We can use binary search to find the smallest substring length. For each
        substring length, we can do a sliding window from left to right and
        check whether the removal of the window at each position results in a
        subsequence of s. Here is where l2r and r2l comes into play. Suppose
        the removed window is from index p to q. We just need to check whether
        l2r[p] >= 0, r2l[q] >= 0, and l2r[p] < r2l[q]. If all three is satisfied
        then we have found a subsequence. And we can shrink the size down.

        Otherwise, if the entire sliding window does not produce a subsequence,
        we have to get the size up.

        There are more nuiances in the actual sliding window (e.g. p shall start
        at -1 and q can end outside t), but that is the gist.

        O(M + N + MlogN), 597 ms, faster than 7.24%
        """
        M, N = len(s), len(t)
        l2r, r2l = [-1] * N, [-1] * N
        i = j = 0
        while i < M and j < N:
            if s[i] == t[j]:
                l2r[j] = i
                i += 1
                j += 1
            else:
                i += 1
        i, j = M - 1, N - 1
        while i >= 0 and j >= 0:
            if s[i] == t[j]:
                r2l[j] = i
                i -= 1
                j -= 1
            else:
                i -= 1
        lo, hi = 0, N + 1
        while lo < hi:
            mid = (lo + hi) // 2
            p, q = -1, mid
            while q <= N:
                if (p >= 0 and l2r[p] < 0) or (q < N and r2l[q] < 0) or (q >= 0 and q < N and l2r[p] >= r2l[q]):
                    p += 1
                    q += 1
                else:
                    break
            else:
                lo = mid + 1
                continue
            hi = mid
        return lo


sol = Solution()
tests = [
    ("abacaba", "bzaa", 1),
    ("cde", "xyz", 3),
    ("aabbbaababb", "bbabab", 0),
    ("aabbbaa", "bbababa", 3),
    ("aabababbbbababababababa", "bababababaabbabbaababba", 6),
    ("babbababab", "ababababab", 1),
    ("acdedcdbabecdbebda", "bbecddb", 1),
]

for i, (s, t, ans) in enumerate(tests):
    res = sol.minimumScore(s, t)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
