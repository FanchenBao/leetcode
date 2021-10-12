# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def guessNumber(self, n: int) -> int:
        """LeetCode 374

        Just binary search.

        O(logN), 46 ms, 18% ranking.
        """
        lo, hi = 1, n
        while lo <= hi:
            mid = (lo + hi) // 2
            ver = guess(mid)
            if ver < 0:
                hi = mid - 1
            elif ver > 0:
                lo = mid + 1
            else:
                return mid



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
