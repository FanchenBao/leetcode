# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        """LeetCode 1328

        Check the first half of palindrome. If any letter is not 'a', swap it
        with 'a'.

        Otherwise, we only swap the last letter with 'a'.

        Edge case is when the palindrome has length of 1, in which case it is
        not breakable.

        O(N), 55 ms, faster than 44.21%
        """
        n = len(palindrome)
        if n == 1:
            return ''
        for i in range(n // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]
        return palindrome[:-1] + 'b'


sol = Solution()
tests = [
    ('abccba', 'aaccba'),
    ('a', ''),
    ('aaaaa', 'aaaab'),
    ('aaabaaa', 'aaabaab'),
    ('abba', 'aaba'),
]

for i, (palindrome, ans) in enumerate(tests):
    res = sol.breakPalindrome(palindrome)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
