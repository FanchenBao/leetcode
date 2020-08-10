#! /usr/bin/env python3
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        for d in dominoes:
            if d[0] > d[1]:
                temp = d[1]
                d[1] = d[0]
                d[0] = temp
        dominoes.sort(key=lambda x: (x[0], x[1]))
        count: int = 0
        i: int = 0
        length: int = len(dominoes)
        while i < length - 1:
            if dominoes[i] != dominoes[i + 1]:
                i += 1
            else:
                repeat = 1
                while i < length - 1 and dominoes[i] == dominoes[i + 1]:
                    repeat += 1
                    i += 1
                if repeat > 1:
                    count += self.comb(repeat, 2)
        return count

    def comb(self, n: int, k: int) -> int:
        return self.fact(n) // (2 * self.fact(n - 2))

    def fact(self, n: int) -> int:
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res


sol = Solution()
print(
    sol.numEquivDominoPairs(
        [[2, 2], [1, 2], [1, 2], [1, 1], [1, 2], [1, 1], [2, 2]]
    )
)
