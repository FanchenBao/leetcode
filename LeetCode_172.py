# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def trailingZeroes(self, n: int) -> int:
        """LeetCode 172

        It took me a while to figure out the trick in this problem. The
        requirement is to do it in log time. Thus, we cannot simply compute the
        factorial for each n. I was thinking about divide and concur, but this
        still requires counting the number of zeroes at each subtask. This does
        not seem to simplify the problem much.

        The insight came when I realized that the only combination to create a
        trailing zero is 2 * 5. And since there are a lot more two factors in
        factorial than five factors, thus the number of trailing zeros equals
        the number of five factors. In other words, we only need to find all
        the five factors from 1 to n.

        We start with number of values in the form of 5 * k. Then 5^2 * k. Then
        5^3 * k, until 5^? is larger than n. For each form, the number of
        additional five factors is n // 5^?.

        O(logN), 20 ms, 99% ranking.
        """
        res, p = 0, 1
        while 5**p <= n:
            res += n // 5**p
            p += 1
        return res


class Solution2:
    def trailingZeroes(self, n: int) -> int:
        """Recursion, same idea, but the implementation is very smart.

        https://leetcode.com/problems/factorial-trailing-zeroes/discuss/52371/My-one-line-solutions-in-3-languages
        """
        return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)


sol = Solution2()
# tests = [
#     (3, 0),
#     (5, 1),
#     (10, 2),
#     (0, 0),
# ]
tests = list(range(1000))

for i, n in enumerate(tests):
    res = sol.trailingZeroes(n)
    facstr = str(math.factorial(n))
    ans = len(facstr) - len(facstr.rstrip('0'))
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
