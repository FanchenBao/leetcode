# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        """LeetCode 1328

        The logic is fairly simple. We go through the first half of the
        palindrome. If palindrome is odd in length, we do not consider the
        center letter. Among the first half, the first letter that is not 'a'
        must be changed to 'a', and we are done.

        If the first half is all 'a's, then we change the last letter of the
        palindrome to 'b'. The tricky part is when the palindrome is of length
        1, in which case we cannot do anything and return empty string.

        O(N), 24 ms, 94% ranking.
        """
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]
        return '' if len(palindrome) == 1 else palindrome[:-1] + 'b'


sol = Solution()
tests = [
    ('abccba', 'aaccba'),
    ('a', ''),
    ('aa', 'ab'),
    ('aba', 'abb')
]

for i, (palindrome, ans) in enumerate(tests):
    res = sol.breakPalindrome(palindrome)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
