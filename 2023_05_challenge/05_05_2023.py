# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """LeetCode 1456

        Sliding window.

        O(N), 219 ms, faster than 43.02% 
        """
        vowel_set = set('aeiou')
        i = cur = res = 0
        for j in range(len(s)):
            if j - i + 1 > k:
                if s[i] in vowel_set:
                    cur -= 1
                i += 1
            if s[j] in vowel_set:
                cur += 1
            res = max(res, cur)
        return res
        

sol = Solution()
tests = [
    ("abciiidef", 3, 3),
    ("aeiou", 2, 2),
    ("leetcode", 3, 2),
]

for i, (s, k, ans) in enumerate(tests):
    res = sol.maxVowels(s, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
