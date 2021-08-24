# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        """LeetCode 537

        Using python's built in complex number to handle. Very
        straightforward.

        32 ms, 50% ranking.
        """
        def convert(num: str) -> complex:
            num_list = num.split('+')
            return complex(int(num_list[0]), int(num_list[1][:-1]))

        res = convert(num1) * convert(num2)

        return str(int(res.real)) + '+' + str(int(res.imag)) + 'i'


class Solution2:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        """Not using the built-in complex number.
        """
        a, b = [int(n) for n in num1[:-1].split('+')]
        c, d = [int(n) for n in num2[:-1].split('+')]
        return str(a * c - b * d) + '+' + str(b * c + a * d) + 'i'


sol = Solution2()
tests = [
    ('1+1i', '1+1i', '0+2i'),
    ('1+-1i', '1+-1i', '0+-2i'),
]

for i, (num1, num2, ans) in enumerate(tests):
    res = sol.complexNumberMultiply(num1, num2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
