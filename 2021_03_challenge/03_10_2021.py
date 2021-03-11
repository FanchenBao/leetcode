# from pudb import set_trace; set_trace()
from typing import List
from bisect import bisect_right


class Solution1:
    def intToRoman(self, num: int) -> str:
        """This is not the best solution. I knew it because I have done this
        problem before, and the best solution does NOT look like this. This is
        just a solution. It starts from the left of the number and going to the
        right. For instance, given a number abcd, we first look at a * 1000 and
        see how that number can be represented. Then we move on to b * 100, c *
        10, and eventually d.

        For each value, we look up in the key list to find the biggest key
        that is smaller than the value. We know for sure, that the biggest key
        that is smaller than the value must be used. So we repeatedly add the
        Roamn symbol represented by the key, and remove the key from the value,
        until the value becomes 0.

        O(N), 56 ms, 39% ranking.
        """
        symbols = {
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
        str_num = str(num)
        power = len(str_num) - 1
        res = ''
        key_lst = list(symbols.keys())
        for d in str_num:
            val = int(d) * 10**power
            while val:
                idx = bisect_right(key_lst, val) - 1
                res += symbols[key_lst[idx]]
                val -= key_lst[idx]
            power -= 1
        return res


class Solution2:
    def intToRoman(self, num: int) -> str:
        """This is the official good solution. In a sense, Solution1 is actually
        in the ballpark of this solution, but we use bisect to locate which key
        to use for the current value. This is not necessary, because it is
        guaranteed that the key to use will always go from the largest to the
        smallest. So we only need to keep a pointer going from the largest key
        downwards and remove as many keys as possible for each value encountered

        This is the third time I have done this problem. I sincerely hope that
        I can remember this solution.
        """
        symbols = {
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
        res = ''
        key_lst = list(symbols.keys())[::-1]
        i = 0
        while num and i < len(key_lst):
            if num >= key_lst[i]:
                res += symbols[key_lst[i]]
                num -= key_lst[i]
            else:
                i += 1
        return res


sol = Solution2()
tests = [
    (3, 'III'),
    (4, 'IV'),
    (9, 'IX'),
    (58, 'LVIII'),
    (1994, 'MCMXCIV'),
]

for i, (num, ans) in enumerate(tests):
    res = sol.intToRoman(num)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
