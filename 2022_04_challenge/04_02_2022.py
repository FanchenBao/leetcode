# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def validPalindrome(self, s: str) -> bool:
        """LeetCode 680

        It's not as easy as I had expected. The idea is to use two pointers
        going towards the center. If s[lo] == s[hi], the current positions at
        both ends satisfy palindrome. Whenever s[lo] != s[hi], that means one
        of the two must be removed. We can remove s[lo] and check whether
        s[hi + 1:lo + 1] is a palindrome. Or we can remove s[hi] and check
        whether s[hi:lo] is a palindrome.

        O(N), 111 ms, 87% ranking.

        UPDATE: reduce a few lines thanks to the official solution
        """
        lo, hi = 0, len(s) - 1
        while lo < hi:
            if s[lo] != s[hi]:
                return s[lo + 1:hi + 1] == s[lo + 1:hi + 1][::-1] or s[lo:hi] == s[lo:hi][::-1]
            lo += 1
            hi -= 1
        return True


sol = Solution()
tests = [
    ('aba', True),
    ('abca', True),
    ('abc', False),
    ('aabb', False),
    ('aabbcc', False),
]

for i, (s, ans) in enumerate(tests):
    res = sol.validPalindrome(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
