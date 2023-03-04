# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """LeetCode 28

        KMP!!

        NOTE: the suffix and prefix do not include the entire string.

        Still requires a lot of assistance to make sense of KMP.
        O(N + M)
        """
        N, M = len(haystack), len(needle)
        pat = [0] * M

        # obtain pattern array, in which pat[i] is the length of prefix that is
        # the same as the suffix ending at needle[i]
        # I can't figure this one out. Had to check reference
        l, j = 0, 1  # l is the length of the prefix
        while j < M:
            if needle[l] == needle[j]:
                l += 1
                pat[j] = l
                j += 1
            else:
                if l > 0:
                    # find the prefix that matches the current suffix of needle[:i]
                    # because that is where the next match to needle[j] would be
                    l = pat[l - 1]
                else:
                    j += 1

        # match
        i = j = 0
        while j < N and i < M:
            if haystack[j] == needle[i]:
                i += 1
                j += 1
            elif i > 0:
                i = pat[i - 1]
            else:
                j += 1
        return j - M if i == M else -1


sol = Solution()
tests = [
    ("sadbutsad", "sad", 0),
    ("leetcode", "leeto", -1),
    ('abc', 'a', 0),
    ('abc', 'b', 1),
    ('abc', 'c', 2),
    ('abc', 'd', -1),
    ("mississippi", "issip", 4),
    ("aabaaabaaac", "aabaaac", 4),
]

for i, (haystack, needle, ans) in enumerate(tests):
    res = sol.strStr(haystack, needle)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
