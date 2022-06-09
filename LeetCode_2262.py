# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict
from bisect import bisect_right


class Solution:
    def appealSum(self, s: str) -> int:
        """This is one of the easier hard problems.

        The idea is DP. Say we have the total appeals of all the substrings
        ending at s[i - 1]. Now we are looking at s[i]. If we count from
        s[i - 1] back until the first letter that is the same as s[i], let's
        say that letter happens at s[j], then we know for sure from s[j + 1]
        till s[i - 1], there is no s[i]. Therefore, all the substrings ending
        at s[i] that starts from within s[j + 1] till s[i - 1] has one more
        appeal than all the substrings that starts from within s[j + 1] and
        ends at s[i - 1]. All the substrings that starts before s[j + 1] and
        ends at s[i] has the same appeal as the substrings that starts before
        s[j + 1] and ends at s[i - 1] (due to s[i] and s[j] being the same).
        Therefore, if we have the total appeal of all the substrings ending
        at s[i - 1], let's call it cur, the total appeal of all the substrings
        ending at s[i] is: cur + i - j

        Now the question is how to find j efficiently. We can use a dict (or
        an array because there are only 26 letters) to record the most recent
        index where a letter appears. If a letter has never appeared before, we
        set the index to -1.

        O(N), 330 ms, faster than 51.77%
        """
        res, cur = 0, 0
        indices = {}
        for i, le in enumerate(s):
            pre_i = indices.get(le, -1)
            cur += i - pre_i
            res += cur
            indices[le] = i
        return res


sol = Solution()
tests = [
    ('abbca', 28),
    ('code', 20),
]

for i, (s, ans) in enumerate(tests):
    res = sol.appealSum(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
