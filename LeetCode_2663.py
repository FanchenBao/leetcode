# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        """We go from right to left. Suppose we are currently at position s[i],
        the pattern of s[i + 1:] is deterministic depending on what s[i] and
        s[i - 1] (if it exists) are.

        The pattern of s[i + 1:] must be a repeat of triplets. The smalleset of
        all is a repeat of 'abc', because any other combinations do not satisfy
        the requirement of no palindrome.

        However, we cannot always use 'abc'. Here are the cases that determine
        which triplet we shall use. Say we have determined that cur is a valid
        letter for s[i], then

        if i - 1 < 0:
            if cur == 'b'  (note that cur can never be 'a'):
                triplet = 'acb'
            else:
                triplet = 'abc'
        else:
            if cur == 'b':
                if s[i - 1] == 'a':
                    triplet = 'cab'
                else:
                    triplet = 'acb'
            else:
                if s[i - 1] == 'a':
                    triplet = 'bac'
                else:
                    triplet = 'abc'

        But before we can follow this rule, we have to make sure cur is valid.
        To make cur valid, we don't have to check the pattern on the right,
        because the triplet choices have already done the check. What we need
        to do is to check the pattern on the left.

        If we have more than two letters on the left, we have to make sure that
        cur != s[i - 1] and cur != s[i - 2]

        If we only have one letter on the left, then cur != s[i - 1].

        If there is nothing on the left, we don't have to check.

        The final solution is to combine all these if-else together and
        implement a mechanism to increment cur if it fails.

        O(N * K), 287 ms, faster than 99.28%
        """
        N = len(s)
        for i in range(N - 1, -1, -1):
            cur = ord(s[i]) - 97 + 1
            while cur < k:
                if i - 1 < 0:
                    if cur == 1:
                        rpat = 'acb'
                    else:
                        rpat = 'abc'
                    break
                elif (i - 1 == 0 and ord(s[i - 1]) - 97 != cur) or (i - 1 > 0 and ord(s[i - 1]) - 97 != cur and ord(s[i - 2]) - 97 != cur):
                    if cur == 1:
                        if ord(s[i - 1]) - 97 == 0:
                            rpat = 'cab'
                        else:
                            rpat = 'acb'
                    else:
                        if ord(s[i - 1]) - 97 == 0:
                            rpat = 'bac'
                        else:
                            rpat = 'abc'
                    break
                cur += 1
            else:
                continue
            q, r = divmod(N - i - 1, 3)
            return s[:i] + chr(cur + 97) + q * rpat + rpat[:r]
        return ''


class Solution2:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        """Inspired by votrubac https://leetcode.com/problems/lexicographically-smallest-beautiful-string/discuss/3468265/Weird-Problem

        His solution also goes right to left. At each position, we check whether
        the current letter is valid. If not valid, we increment it, until we
        can't, at which time we move to the previous letter.

        The check itself is not complicated. We already solved it, but he used
        a much cleaner way to express it.

        The real genius is that once a letter is confirmed, we can create the
        rest of the string on the right side using the exact same logic. In
        other words, we don't have to figure out the different patterns.

        It's going to be slower for sure, because the creation of the pattern
        speeds up the filling of the rest of the string. But creating the rest
        of the string automatically should be the first solution, and figuring
        out the pattern should be a performance boost.

        O(N), 482 ms, faster than 76.81%
        """
        lst_s = list(s)

        def check(idx: int, le: str) -> bool:
            return idx < 1 or (lst_s[idx - 1] != le and (idx < 2 or lst_s[idx - 2] != le))
        
        for i in range(len(s) - 1, -1, -1):
            cur = ord(s[i]) + 1
            while not check(i, chr(cur)):
                cur += 1
            if cur < k + 97:
                lst_s[i] = chr(cur)
                for j in range(i + 1, len(s)):
                    for p in range(k):
                        if check(j, chr(p + 97)):
                            lst_s[j] = chr(p + 97)
                            break
                return ''.join(lst_s)
        return ''


class Solution3:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        """Same as solution2 to find the correct current letter. And then we use
        the pattern from solution1 to speed things up.

        401 ms, faster than 84.78%
        """
        def check(idx: int, le: str) -> bool:
            return idx < 1 or (s[idx - 1] != le and (idx < 2 or s[idx - 2] != le))
        
        for i in range(len(s) - 1, -1, -1):
            cur = ord(s[i]) + 1
            while not check(i, chr(cur)):
                cur += 1
            if cur < k + 97:
                cur_le = chr(cur)
                if i < 1:
                    rpat = 'acb' if cur_le == 'b' else 'abc'
                else:
                    if cur_le == 'b':
                        rpat = 'cab' if s[i - 1] == 'a' else 'acb'
                    else:
                        rpat = 'bac' if s[i - 1] == 'a' else 'abc'
                q, r = divmod(len(s) - i - 1, 3)
                return s[:i] + cur_le + q * rpat + rpat[:r]
        return ''


sol = Solution3()
tests = [
    ('abcz', 26, 'abda'),
    ('dc', 4, ''),
    ('abca', 4, 'abcd'),
    ('b', 6, 'c'),
    ("dacd", 4, 'dbac'),
]

for i, (s, k, ans) in enumerate(tests):
    res = sol.smallestBeautifulString(s, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
