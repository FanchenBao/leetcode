# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def intToRoman(self, num: int) -> str:
        """LeetCode 12

        O(logN), 107 ms, faster than 33.64%
        """
        base = 1
        res = ''
        hashmap = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M',
        }
        while num:
            num, r = divmod(num, 10)
            val = r * base
            if val in hashmap:
                res += hashmap[val][::-1]
            else:
                if r < 5:
                    res += (hashmap[base] * r)[::-1]
                else:
                    res += (hashmap[base * 5] + hashmap[base] * (r - 5))[::-1]
            base *= 10
        return res[::-1]


class Solution2:
    def intToRoman(self, num: int) -> str:
        """This method comes from the previous attempt at this problem on
        2021-03-10. I like this one better.

        123 ms, faster than 14.87%
        """
        res = ''
        hashmap = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I',
        }
        i = 0
        keys = list(hashmap.keys())
        while num and i < len(keys):
            if num >= keys[i]:
                res += hashmap[keys[i]]
                num -= keys[i]
            else:
                i += 1
        return res


sol = Solution2()
tests = [
    (3, 'III'),
    (58, 'LVIII'),
    (1994, 'MCMXCIV'),
]

for i, (num, ans) in enumerate(tests):
    res = sol.intToRoman(num)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
