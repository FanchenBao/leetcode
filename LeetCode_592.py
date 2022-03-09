# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter
import math


class Solution:
    def fractionAddition(self, expression: str) -> str:
        """First, we preprocess the expression by extracting each fraction
        number. But we can do this smartly by using the denominator as key and
        nominator as value in a hashmap, such that we can easily compute the
        sum of all fractions that have the same denominator.

        After that, we compute the sum of all the key-value pairs in the
        hashmap, using GCD to reduce a fraction.

        O(NlogM), where N is the number of fraction numbers, and logM is the
        max cost of math.gcd.

        45 ms, 55% ranking.
        """
        hashmap = Counter()
        pre = 0
        for i in range(1, len(expression)):
            if expression[i] in '-+':
                nom, den = expression[pre:i].split('/')
                hashmap[int(den)] += int(nom)
                pre = i
        nom, den = expression[pre:].split('/')
        hashmap[int(den)] += int(nom)
        res_nom, res_den = 0, 1
        for den, nom in hashmap.items():
            if den:
                res_nom, res_den = res_nom * den + nom * res_den, den * res_den
                gcd_ = math.gcd(res_nom, res_den)
                res_nom //= gcd_
                res_den //= gcd_
        return f'{res_nom}/{res_den}'
        

sol = Solution()
tests = [
    ("-1/2+1/2", '0/1'),
    ('-1/2+1/2+1/3', '1/3'),
    ('1/3-1/2', '-1/6'),
]

for i, (expression, ans) in enumerate(tests):
    res = sol.fractionAddition(expression)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
