# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter, deque


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """LeetCode 76

        A more advanced sliding window. We need to first find the window s[0:i]
        where all letters in t is in s. Also, we use a deque to keep track of
        all the letters in t that have been encountered in s.

        Then, if we encounter any additional letter in s that is also in t, we
        check whether some letters on the front of the deque has more copies
        in the current window than t. If that is the case, we pop the front
        until we are not able to do so anymore. This reduces the size of the
        window. Then we can check whether the new window is smaller than the
        previous one. If it is, we keep the left and right indices of the
        new window.

        In implementation, we use a set called unmatched_t to determine if the
        first window s[0:i] has been acquired. If the first window has not been
        acquired, we will not update the left and right indices.

        O(M + N), 192 ms, faster than 64.96%

        UPDATE: the official solution as coded by myself a year and 2 months
        ago used the idea of shrinking s to a version where only the letter in
        t exists. Then, a sliding window with l and r pointers are used, where
        r keeps going right, and l goes right if the remaining window still
        satisfies t. This is almost exactly the same idea as the current
        solution. In fact, deq is a version of the shrunken array, except we
        use popleft to handle the sliding window, instead of incrementing the
        l index.
        """
        deq = deque()
        sc = Counter()
        tc = Counter(t)
        rl, rr = -math.inf, math.inf
        unmatched_t = set(t)
        for i, le in enumerate(s):
            if le in tc:
                deq.append(i)
                sc[le] += 1
                if le in unmatched_t and sc[le] >= tc[le]:
                    unmatched_t.remove(le)
                while deq and sc[s[deq[0]]] > tc[s[deq[0]]]:
                    sc[s[deq.popleft()]] -= 1
                if deq[-1] - deq[0] < rr - rl and not unmatched_t:
                    rl, rr = deq[0], deq[-1]
        return s[rl:rr + 1] if not unmatched_t else ''


sol = Solution()
tests = [
    ("ADOBECODEBANC", "ABC", 'BANC'),
    ("a", "a", 'a'),
    ("a", "aa", ''),
    ("cabwefgewcwaefgcf", "cae", "cwae"),
    ("acbbaca", "aba", "baca"),
]

for i, (s, t, ans) in enumerate(tests):
    res = sol.minWindow(s, t)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
