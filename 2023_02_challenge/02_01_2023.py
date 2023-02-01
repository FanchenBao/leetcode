# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """LeetCode 1071

        Go through all possible lengths of gcd string one by one. A candidate
        length must divide the length of str1 and str2. Once a candidate length
        is found, we use set to see whether str1 and str2 can be formed by
        concatenating the same string.

        O(N^2), 31 ms, faster than 86.37%
        """
        if len(str1) < len(str2):
            str1, str2 = str2, str1  # ensure str2 is shorter
        for n in range(len(str2), 0, -1):
            if len(str2) % n == 0 and len(str1) % n == 0:
                div1 = set(str1[i:i + n] for i in range(0, len(str1), n))
                if len(div1) > 1:
                    continue
                div2 = set(str2[i:i + n] for i in range(0, len(str2), n))
                if len(div2) > 1:
                    continue
                d1, d2 = list(div1)[0], list(div2)[0]
                if d1 == d2:
                    return d1
        return ''


class Solution2:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """Solution from the official solution.

        Use str1 + str2 == str2 + str1 to check whether a gcd string exists.
        If it exists, then the length of the gcd string must be the gcd of the
        length of str1 and str2.
        """
        return str1[:math.gcd(len(str1), len(str2))] if str1 + str2 == str2 + str1 else ''


sol = Solution2()
tests = [
    ("ABCABC", "ABC", 'ABC'),
    ("ABABAB", "ABAB", 'AB'),
    ("LEET", "CODE", '')
]

for i, (str1, str2, ans) in enumerate(tests):
    res = sol.gcdOfStrings(str1, str2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
