# from pudb import set_trace; set_trace()
from typing import List
from bisect import bisect_left
from collections import defaultdict


class Solution1:
    def isSubsequence(self, s: str, t: str) -> bool:
        """LeetCode 392

        This is quite naive solution and feels stupid to me.

        O(M) where M = len(t), 78 ms, 8% ranking.
        """
        i = 0
        N = len(s)
        if N > len(t):
            return False
        for le in t:
            if i < N and le == s[i]:
                i += 1
                if i == N:
                    break
        return i == N


class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        """This can solve the follow up question. We build a hashmap for each
        letter in t and all indices of its occurences. Then we can
        compare each letter in s to the hashmap using binary search. This way,
        we build the hashmap once, and can run the checking for all s in
        O(len(s) * log(len(t))) time.

        60 ms, 23% ranking.
        """
        if len(s) > len(t):
            return False
        hashmap = defaultdict(list)
        for i, le in enumerate(t):
            hashmap[le].append(i)
        cur_idx = 0
        for le in s:
            if le not in hashmap:
                return False
            idx = bisect_left(hashmap[le], cur_idx)
            if idx == len(hashmap[le]):
                return False
            cur_idx = hashmap[le][idx] + 1
        return True


sol = Solution2()
tests = [
    ("abc", "ahbgdc", True),
    ("axc", "ahbgdc", False),
    ('abc', 'ab', False),
    ('', '', True),
    ('', 'a', True),
    ('a', '', False),
    ('ab', 'baab', True),
    ("acb", "ahbgdc", False),
]

for i, (s, t, ans) in enumerate(tests):
    res = sol.isSubsequence(s, t)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
