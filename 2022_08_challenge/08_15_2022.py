# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def romanToInt(self, s: str) -> int:
        """LeetCode 13

        45 ms, faster than 96.74%
        """
        rules = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }
        res, i = 0, 0
        while i < len(s):
            if s[i:i + 2] in {'IV', 'IX', 'XL', 'XC', 'CD', 'CM'}:
                res += rules[s[i:i + 2]]
                i += 2
            else:
                res += rules[s[i]]
                i += 1
        return res


sol = Solution()
tests = [
    ('III', 3),
    ('LVIII', 58),
    ('MCMXCIV', 1994),
]

for i, (s, ans) in enumerate(tests):
    res = sol.romanToInt(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
