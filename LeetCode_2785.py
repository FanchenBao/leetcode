# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def sortVowels(self, s: str) -> str:
        """
        Find all the vowels, sort them, and put them back in the
        original string where the vowels are from left to right
        
        O(NlogN), 119 ms, faster than 91.58%
        """
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        slist = list(s)
        vs = []
        for le in slist:
            if le in vowels:
                vs.append(le)
        vs.sort(reverse=True)
        for i, le in enumerate(slist):
            if le in vowels:
                slist[i] = vs.pop()
        return ''.join(slist)


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
