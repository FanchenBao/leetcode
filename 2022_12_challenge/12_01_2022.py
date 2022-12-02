# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution1:
    def halvesAreAlike(self, s: str) -> bool:
        """LeetCode 1704

        82 ms, faster than 22.49%
        """
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        cl, cr = 0, 0
        N = len(s)
        for i in range(N // 2):
            cl += int(s[i] in vowels)
            cr += int(s[i + N // 2] in vowels)
        return cl == cr


class Solution2:
    def halvesAreAlike(self, s: str) -> bool:
        """50 ms, faster than 76.05% 
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        N = len(s)
        cl = Counter(s[:N // 2])
        cr = Counter(s[N // 2:])
        return sum(cl[v] for v in vowels) == sum(cr[v] for v in vowels)
        

sol = Solution2()
tests = [
    ("book", True),
    ("textbook", False),
]

for i, (s, ans) in enumerate(tests):
    res = sol.halvesAreAlike(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
