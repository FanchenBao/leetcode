# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def minimumLength(self, s: str) -> int:
        """We use two pointers and we move the pointers towards the center. At
        each moment, we check whether the values at the two pointers are the
        same. If they are not the same, that means we cannot proceed anymore.
        If they are the same, then we skip all the duplicates for both pointers
        and land on new letters. Then we continue.

        O(N), 116 ms, 51% ranking.
        """
        lo, hi = 0, len(s) - 1
        while lo < hi and s[lo] == s[hi]:
            while lo + 1 < hi and s[lo] == s[lo + 1]:
                lo += 1
            while hi - 1 > lo and s[hi] == s[hi - 1]:
                hi -= 1
            lo += 1
            hi -= 1
        return hi - lo + 1        


sol = Solution()
tests = [
    ('ca', 2),
    ('cabaabac', 0),
    ('aabccabba', 3),
    ('a', 1),
    ('aa', 0),
    ('aaa', 0),
]

for i, (s, ans) in enumerate(tests):
    res = sol.minimumLength(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
