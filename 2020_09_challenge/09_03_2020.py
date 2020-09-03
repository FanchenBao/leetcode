# from pudb import set_trace; set_trace()
from typing import List
from collections import deque


class Solution1:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """Pass OJ with 864 ms runtime."""
        size = len(s)
        poten = deque()
        for i, le in enumerate(s):
            for _ in range(len(poten)):
                pat = poten.popleft()
                if le == pat[i % len(pat)]:
                    poten.append(pat)
            if size % (i + 1) == 0 and size != i + 1:  # has potential
                poten.append((s[:i + 1]))
        return True if poten else False


class Solution2:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """Use KMP pattern table built up"""
        n = len(s)
        lps = [0] * n
        # i is the index of the current prefix element to be matched.
        # i + 1 is the length of the prefix that has been matched on suffix
        i = 0
        j = 1  # j is the progressing index on s to find match with i.
        while j < n:
            if s[j] == s[i]:
                lps[j] = i + 1
                i += 1
                j += 1
            else:
                if i != 0:
                    # go to i - 1, which is the last element that potentially
                    # matches. Look into lps[i - 1], we get the number of
                    # prefixes that has matched until i - 1. This means index
                    # lps[i - 1] - 1 is the previous index starting from the
                    # beginning that has been matched before the current mis-
                    # match. Then the next element to compare to the current
                    # mis-match is lps[i - 1] - 1 + 1 = lps[i - 1]
                    i = lps[i - 1]
                else:
                    j += 1
        # If s is repeats of some prefix, lps shall end up looking like this
        # [0, 0, ..., 0, 1, 2, 3, 4, ..., m] where m = n - len(prefix)
        return lps[-1] and n % (n - lps[-1]) == 0


class Solution3:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """The brain-twister smart-ass way"""
        return s in (s + s)[1 : -1]



sol = Solution3()
tests = [
    ('abab', True),
    ('aba', False),
    ('abcabcabcabc', True),
    ('abcabcababcabcab', True),
    ('abcbac', False),
    ('aabaabaab', True),
    ('a', False),
    ('aaaaaaa', True),
    ('aaaaab', False),
]

for i, (s, ans) in enumerate(tests):
    res = sol.repeatedSubstringPattern(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
