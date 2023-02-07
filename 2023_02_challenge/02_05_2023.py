# from pudb import set_trace; set_trace()
from typing import List
import math
from collection import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """LeetCode 438

        Sliding window.

        O(N), where N = len(s), 378 ms, faster than 31.63%
        """
        M = len(p)
        if M > len(s):
            return []
        cp = Counter(p)
        cs = Counter(s[:M])
        res = []
        if cp == cs:
            res.append(0)
        for i in range(M, len(s)):
            cs[s[i]] += 1
            cs[s[i - M]] -= 1
            if not cs[s[i - M]]:
                del cs[s[i - M]]
            if cs == cp:
                res.append(i - M + 1)
        return res


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
