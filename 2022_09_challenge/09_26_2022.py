# from pudb import set_trace; set_trace()
from typing import List
import math


class DSU:
    def __init__(self, n: int) -> None:
        self.par = list(range(n))
        self.rnk = [0] * n

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # no need to union, already together
        if self.rnk[px] > self.rnk[py]:
            self.par[py] = px
        elif self.rnk[px] < self.rnk[py]:
            self.par[px] = py
        else:
            self.rnk[px] += 1
            self.par[py] = px
        return True


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        """LeetCode 990

        Not a difficult problem using union find. The most difficult part is
        still writing DSU from scratch. I almost got it, but made a mistake in
        the union method.

        The idea is that we union all the letters that are connected by '=='
        sign first. Then we go through the inequalities. And if a pair of not
        equal letters actually belong to the same union, we return False.

        O(N), the union find complexity is alpha(26), which is essentially O(1)
        89 ms, faster than 34.34%
        """
        equations.sort(key=lambda eq: eq[1], reverse=True)
        dsu = DSU(26)
        for eq in equations:
            if eq[1] == '=':
                dsu.union(ord(eq[0]) - 97, ord(eq[3]) - 97)
            elif dsu.find(ord(eq[0]) - 97) == dsu.find(ord(eq[3]) - 97):
                # equation says they are different, but they belong to the
                # same group
                return False
        return True


sol = Solution()
tests = [
    (["a==b","b!=a"], False),
    (["b==a","a==b"], True),
    (["a==b","e==c","b==c","a!=e"], False),
]

for i, (equations, ans) in enumerate(tests):
    res = sol.equationsPossible(equations)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
