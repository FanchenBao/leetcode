# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict, deque


class Solution1:
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


class Solution2:
    def minimumScore(self, s: str, t: str) -> int:
        """Sliding window with O(N) complexity.

        Ref: https://leetcode.com/problems/subsequence-with-the-minimum-score/discuss/3174041/Right-and-Left-O(n)

        We do r2l the same way as in solution1. But, then we do l2r and find the
        result directly.

        Suppose r2l[k] is the final index in s that matches t[k]. Each time in
        l2r, when s[i] == t[j], we need to see whether i < r2l[k]. If it is,
        then we can take s[i] == t[j] and move both indices forward (i.e.
        shrinking the window). However, if i >= r2l[k], then k needs to move
        forward until i < r2l[k] (i.e., broadening the window).

        O(N), 160 ms, faster than 78.46%
        """
        M, N = len(s), len(t)
        r2l = [-1] * N
        i, k = M - 1, N - 1
        while i >= 0 and k >= 0:
            if s[i] == t[k]:
                r2l[k] = i
                i -= 1
                k -= 1
            else:
                i -= 1
        k += 1  # r2l[k] points to the final index in s that matches t[k]
        if k == 0:  # t is already a subsequence of s
            return 0
        i = j = 0
        res = k
        while i < M and j < N:
            if s[i] == t[j]:
                while k < N and r2l[k] <= i:
                    k += 1
                # print(i, j, k)
                res = min(res, k - j - 1)
                i += 1
                j += 1
            else:
                i += 1
        return res


sol = Solution2()
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
