# from pudb import set_trace; set_trace()
from typing import List
from functools import reduce
from operator import mul


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        """Given n digit number. The first position has 9 choices (0-9, but we
        cannot take 0). The second position also has 9 choices (0-9, but we
        cannot take the number on the first position). The third position has
        8 choices, the fourth 7, ...

        Thus the number of unique values in n digit is 9 * 9 * 8 * ... until
        all digits are considered.

        The special case happens when n = 0, which has 1 unique value.

        O(1), 55 ms, 16% ranking.
        """
        return sum((9 if i else 1) * reduce(mul, range(9, 10 - i, -1), 1) for i in range(n + 1))


sol = Solution()
tests = [
    (0, 1),
    (1, 10),
    (2, 91),
    (3, 739),
    (4, 5275),
]

for i, (n, ans) in enumerate(tests):
    res = sol.countNumbersWithUniqueDigits(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
