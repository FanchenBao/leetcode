# from pudb import set_trace; set_trace()
from typing import List
import re


class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        """Once you use regex, now you have two problems. Regex is not easy.

        Lots of trial and error on regex101.com

        254 ms, faster than 40.17%
        """
        
        def repl(m):
            rep = float(m.group(2)) * (100 - discount) / 100
            return f'${rep:.2f}'

        return re.sub(r'(^|(?<=\s))\$(\d+)(?=\s|$)', repl, sentence)



sol = Solution()
tests = [
    ("$1 there are $1 $2$3 and 5$ candies in the shop $7", 33, "$0.67 there are $0.67 $2$3 and 5$ candies in the shop $4.69"),
]

for i, (sentence, discount, ans) in enumerate(tests):
    res = sol.discountPrices(sentence, discount)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
