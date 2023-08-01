# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        """Two pointers and change the corresponding letters to the smaller one.

        O(N), 130 ms, faster than 96.47%
        """
        lst_s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if lst_s[i] != lst_s[j]:
                lst_s[i] = lst_s[j] = min(lst_s[i], lst_s[j])
            i += 1
            j -= 1
        return ''.join(lst_s)


# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
