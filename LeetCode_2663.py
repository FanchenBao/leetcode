# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
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

        If cur == 'b' (note that cur can never be 'a'):
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

        O(N * K), 355 ms, faster than 90.58%
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


sol = Solution()
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
