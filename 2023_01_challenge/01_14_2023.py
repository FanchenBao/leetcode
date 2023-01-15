# from pudb import set_trace; set_trace()
from typing import List
import math


class DSU:
    def __init__(self, n) -> None:
        self.par = list(range(n))
        # self.rnk = [0] * n

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if px < py:
            self.par[py] = px
        else:
            self.par[px] = py
        return True


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        """LeetCode 1061

        Use union-find. Need to modify union a little bit so that the parent
        also prefers a smaller letter

        45 ms, faster than 77.59% 
        """
        dsu = DSU(26)
        for a, b in zip(s1, s2):
            dsu.union(ord(a) - 97, ord(b) - 97)
        return ''.join(chr(dsu.find(ord(le) - 97) + 97) for le in baseStr)


sol = Solution()
tests = [
    ("parker", "morris", "parser", "makkek"),
    ("hello", "world", "hold", "hdld"),
    ("leetcode", "programs", "sourcecode", "aauaaaaada"),
]

for i, (s1, s2, baseStr, ans) in enumerate(tests):
    res = sol.smallestEquivalentString(s1, s2, baseStr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
