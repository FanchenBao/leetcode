# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """LeetCode 567

        Sliding window s2 and check whether each is a permutation of s1.

        O(MN), 1430 ms, faster than 23.38%

        UPDATE: no need to compute new counter each time. Slide window it!!
        O(M), M = len(s2), 109 ms, faster than 55.15%
        """
        N = len(s1)
        if N > len(s2):
            return False
        cs1 = Counter(s1)
        cs2 = Counter(s2[:N])
        if cs1 == cs2:
            return True
        for i in range(N, len(s2)):
            cs2[s2[i]] += 1
            cs2[s2[i - N]] -= 1
            if cs2 == cs1:
                return True
        return False


sol = Solution()
tests = [
    ("ab", "eidbaooo", True),
    ("ab", "eidboaoo", False),
]

for i, (s1, s2, ans) in enumerate(tests):
    res = sol.checkInclusion(s1, s2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
