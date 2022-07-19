# from pudb import set_trace; set_trace()
from typing import List
from fractions import Fraction
from math import gcd


class Solution1:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        """Sort and then compute slope between consecutive pairs. If the slope
        is the same as previous, we are on the same line. Otherwise, create a
        new line.

        O(NlogN), because we sort at the beginning.
        3678 ms, faster than 5.02%
        """
        N = len(stockPrices)
        if N == 1:
            return 0
        if N == 2:
            return 1
        stockPrices.sort()
        s = Fraction(stockPrices[1][1] - stockPrices[0][1], stockPrices[1][0] - stockPrices[0][0])
        res = 1
        for i in range(2, N):
            tmp = Fraction(stockPrices[i][1] - stockPrices[i - 1][1], stockPrices[i][0] - stockPrices[i - 1][0])
            if tmp != s:
                res += 1
                s = tmp
        return res


class Solution2:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        """Try using gcd instead of Fraction.

        Still O(NlogN), but it's much faster: 2233 ms, faster than 66.49%

        This shows that Fraction has a huge overhead.
        """
        N = len(stockPrices)
        if N == 1:
            return 0
        if N == 2:
            return 1
        stockPrices.sort()
        dy, dx = stockPrices[1][1] - stockPrices[0][1], stockPrices[1][0] - stockPrices[0][0]
        g = gcd(dy, dx)
        s = (dy // g, dx // g)
        res = 1
        for i in range(2, N):
            dy, dx = stockPrices[i][1] - stockPrices[i - 1][1], stockPrices[i][0] - stockPrices[i - 1][0]
            g = gcd(dy, dx)
            tmp = (dy // g, dx // g)
            if tmp != s:
                res += 1
                s = tmp
        return res


class Solution3:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        """This comment inspired me to try yet another way. No need to Fraction
        or gcd, because we can do cross multiplication.

        Ref: https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/discuss/2061883/Hidden-Test-Case-!!/1401008
        """
        N = len(stockPrices)
        if N == 1:
            return 0
        if N == 2:
            return 1
        stockPrices.sort()
        dy, dx = stockPrices[1][1] - stockPrices[0][1], stockPrices[1][0] - stockPrices[0][0]
        res = 1
        for i in range(2, N):
            dy_, dx_ = stockPrices[i][1] - stockPrices[i - 1][1], stockPrices[i][0] - stockPrices[i - 1][0]
            if dy * dx_ != dy_ * dx:
                res += 1
                dy, dx = dy_, dx_
        return res


sol = Solution3()
tests = [
    ([[3,4],[1,2],[7,8],[2,3]], 1),
    ([[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]], 3)
]

for i, (stockPrices, ans) in enumerate(tests):
    res = sol.minimumLines(stockPrices)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
