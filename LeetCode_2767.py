# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        """
        Since s has max length of 15, this means there are only seven different
        possible power of five that are within the range for s. Therefore, we
        can try these seven power of fives one by one for the string. If we have
        a match, we divide the string into two additional substrings, which will
        undergo the same process as before. We keep track of the smallest number
        of substrings throughout the entire process.

        We use memoization to reduce the amount of computation.

        O(N^3 * 7), 50 ms, faster than 71.60%
        """
        bases = [
            '1',
            '101',
            '11001',
            '1111101',
            '1001110001',
            '110000110101',
            '11110100001001',
        ]

        @lru_cache(maxsize=None)
        def helper(substr: str) -> int:
            if not substr:
                return 0
            res = math.inf
            for b in bases:
                idx = substr.find(b)
                if idx >= 0:
                    left = substr[:idx]
                    right = substr[idx + len(b):]
                    res = min(res, 1 + helper(left) + helper(right))
            return res

        res = helper(s)
        return res if res < math.inf else -1



sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
