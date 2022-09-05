# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    below_20 = {
        '': '',
        '1': 'One',
        '2': 'Two',
        '3': 'Three',
        '4': 'Four',
        '5': 'Five',
        '6': 'Six',
        '7': 'Seven',
        '8': 'Eight',
        '9': 'Nine',
        '10': 'Ten',
        '11': 'Eleven',
        '12': 'Twelve',
        '13': 'Thirteen',
        '14': 'Fourteen',
        '15': 'Fifteen',
        '16': 'Sixteen',
        '17': 'Seventeen',
        '18': 'Eighteen',
        '19': 'Nineteen',
    }
    multiple_of_tens = {
        '2': 'Twenty',
        '3': 'Thirty',
        '4': 'Forty',
        '5': 'Fifty',
        '6': 'Sixty',
        '7': 'Seventy',
        '8': 'Eighty',
        '9': 'Ninety',
    }

    def convert_two_digits(self, num_str: str) -> str:
        """num_str is at most two digits"""
        if len(num_str) <= 1 or num_str[0] == '1':
            return self.below_20[num_str]
        if num_str[1] == '0':  # handle 20, 30, 40, ..., 90
            return self.multiple_of_tens[num_str[0]]
        return self.multiple_of_tens[num_str[0]] + ' ' + self.below_20[num_str[1]]

    def convert_three_digits(self, num_str: str) -> str:
        """num_str is at most three digits"""
        fdig = f'{self.convert_two_digits(num_str[0])} Hundred' if len(num_str) == 3 else ''
        rem = self.convert_two_digits(num_str[-2:].lstrip("0"))
        if fdig and rem:
            return f'{fdig} {rem}'
        return fdig + rem

    def numberToWords(self, num: int) -> str:
        """This problem is not hard in terms of the actual logic, but quite
        challenging to come up with sufficient test cases.

        65 ms, faster than 19.13%
        """
        if num == 0:
            return 'Zero'
        num_str = str(num)
        res = ''
        levels = ['Billion', 'Million', 'Thousand', '']
        while num_str:
            num_str, cur = num_str[:-3], num_str[-3:].lstrip('0')
            cur_converted = self.convert_three_digits(cur)
            if cur_converted:
                res = f'{cur_converted} {levels.pop()} {res}'
            else:
                levels.pop()
        return res.strip()


sol = Solution()
tests = [
    (0, 'Zero'),
    (123, "One Hundred Twenty Three"),
    (12345, "Twelve Thousand Three Hundred Forty Five"),
    (1234567, "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"),
    (5005, 'Five Thousand Five'),
    (90909909, 'Ninety Million Nine Hundred Nine Thousand Nine Hundred Nine'),
    (30300303, 'Thirty Million Three Hundred Thousand Three Hundred Three'),
    (10000001, 'Ten Million One'),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.numberToWords(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
