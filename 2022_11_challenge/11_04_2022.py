# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def reverseVowels(self, s: str) -> str:
        """LeetCode 345

        Don't forget to include the upper case as well.

        O(N), 95 ms, faster than 70.04%
        """
        lst = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        vowel_indices = [i for i, a in enumerate(s) if a in vowels]
        j = len(vowel_indices) - 1
        for i in vowel_indices:
            lst[i] = s[vowel_indices[j]]
            j -= 1
        return ''.join(lst)


class Solution2:
    def reverseVowels(self, s: str) -> str:
        """Two pointers directly on s
        """
        lst = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] in vowels and s[j] in vowels:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j -= 1
            else:
                if s[i] not in vowels:
                    i += 1
                if s[j] not in vowels:
                    j -= 1
        return ''.join(lst)


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
