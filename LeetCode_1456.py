# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """Basic sliding window

        O(N), 308 ms, faster than 73.31%
        """
        res = -math.inf
        cur = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        i = 0
        for j in range(len(s)):
            cur += int(s[j] in vowels)
            if j - i + 1 > k:
                cur -= int(s[i] in vowels)
                i += 1
            res = max(res, cur)
        return res 


sol = Solution()
tests = [
    ("abciiidef", 3, 3),
    ("aeiou", 2, 2),
    ("leetcode", 3, 2)
]

for i, (s, k, ans) in enumerate(tests):
    res = sol.maxVowels(s, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
