# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        has_odd = False
        res = 0
        for c in counter.values():
            if c % 2:
                res += c - 1
                has_odd = True
            else:
                res += c
        return res + 1 if has_odd else res


sol = Solution()
print(sol.longestPalindrome('bbbggghhhjkmmnnnrrtttuyyy'))
