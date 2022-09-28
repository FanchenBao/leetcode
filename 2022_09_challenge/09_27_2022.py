# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def pushDominoes(self, dominoes: str) -> str:
        """LeetCode 838

        We go from left to right. We maintain the most recent L or R that has
        been encountered. If the current is L and previous is also L, that
        means all the dominoes in between must also be L. If the previous is R,
        that means the dominoes in between fall on each other. Depending on
        whether there are even or odd number of dominoes, we have half R and
        half L, with the middle being dot if the number is odd.

        Similarly, if the current is R and prevous is also R, that means all
        the dominoes in between are R. If previous is L, than all the dominoes
        in between are dots.

        The only trickly part is that we need to extend dominoes by a single
        R such that we can handle the situation where there are dots trailing
        at the end of the string.

        O(N), 244 ms, faster than 92.99%
        """
        dominoes += 'R'
        res = []
        left = 'L'
        for i, d in enumerate(dominoes):
            if d == 'L':
                k = i - len(res)
                if left == 'L':
                    for _ in range(k):
                        res.append('L')
                else:
                    for _ in range(k // 2):
                        res.append('R')
                    if k % 2:
                        res.append('.')
                    for _ in range(k // 2):
                        res.append('L')
                left = 'L'
                res.append('L')
            elif d == 'R':
                for _ in range(i - len(res)):
                    res.append('R' if left == 'R' else '.')
                left = 'R'
                res.append('R')
        res.pop()
        return ''.join(res)


class Solution2:
    def pushDominoes(self, dominoes: str) -> str:
        """Use string directly, instead of list.

        Faster. 199 ms, faster than 99.30% 
        """
        dominoes += 'R'
        res = ''
        left = 'L'
        for i, d in enumerate(dominoes):
            if d == '.':
                continue
            k = i - len(res)
            if d == 'L':
                if left == 'L':
                    res += 'L' * k
                else:
                    res += 'R' * (k // 2) + '.' * (k % 2) + 'L' * (k // 2)
            elif d == 'R':
                res += ('R' if left == 'R' else '.') * k
            left = d
            res += d
        return res[:-1]


sol = Solution2()
tests = [
    ("RR.L", "RR.L"),
    (".L.R...LR..L..", "LL.RR.LLRRLL.."),
]

for i, (dominoes, ans) in enumerate(tests):
    res = sol.pushDominoes(dominoes)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
