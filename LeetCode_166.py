# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        """LeetCode 166

        Not too hard a question, but the negative cases did catch me off
        guard. But negative cases can be easily handled by checking the
        positiveness of the result at the beginning, and then treat both
        numerator and denominator as positive values.

        We perform long division and stop when a remainder has repeated. Also,
        for each remainder, we keep track of its index in the result string.

        I wanted to use the decimal library but the process of finding the exact
        repeating pattern is much harder than I had expected.

        24 ms, 97% ranking.
        """
        is_pos = numerator * denominator >= 0
        n, d = abs(numerator), abs(denominator)
        q, n = divmod(n, d)
        if n == 0:
            return f'{q}' if is_pos else f'-{q}'
        res = f'{q}.'
        hashmap = {}
        i = len(res)
        while n != 0 and n not in hashmap:
            hashmap[n] = i
            q, n = divmod(n * 10, d)
            res += str(q)
            i += 1
        if n != 0:
            res = res[:hashmap[n]] + '(' + res[hashmap[n]:] + ')'
        return res if is_pos else '-' + res


sol = Solution()
tests = [
    (1, 2, '0.5'),
    (2, 1, '2'),
    (2, 3, '0.(6)'),
    (4, 333, '0.(012)'),
    (1, 5, '0.2'),
    (22, 70, '0.3(142857)'),
    (-1, 2, '-0.5'),
    (-50, 8, '-6.25'),
    (0, -10, '0'),
    (-4, -333, '0.(012)'),
]

for i, (numerator, denominator, ans) in enumerate(tests):
    res = sol.fractionToDecimal(numerator, denominator)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
