# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class DSU1:
    def __init__(self) -> None:
        self.par = {}
        self.rnk = defaultdict(int)
        self.val = defaultdict(lambda: -1)

    def find(self, x: int) -> int:
        if x not in self.par:
            self.par[x] = x
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int, v: float) -> bool:
        px, py = self.find(x), self.find(y)
        if px != py:
            # handle values of x and y. This must happen before union, because
            # we only want to update the value in the current subgroup, and then
            # union the two subgroups. If we union first, then the update
            # happens to both subgroups, which we do not want, since one of the
            # subgroups serves as the base.
            if self.val[x] >= 0 and self.val[y] < 0:
                self.val[y] = self.val[x] / v
            elif self.val[y] >= 0 and self.val[x] < 0:
                self.val[x] = self.val[y] * v
            elif self.val[x] < 0 and self.val[y] < 0:
                self.val[y] = 1.0
                self.val[x] = v
            elif not math.isclose(self.val[x] / self.val[y], v, rel_tol=1e-4):
                # both x and y already have value. but we need to scake x and
                # all the numbers associated with x
                ratio = v * self.val[y] / self.val[x]
                for syb in self.par:
                    if self.find(syb) == px:
                        self.val[syb] *= ratio
            if self.rnk[px] > self.rnk[py]:
                self.par[py] = px
            elif self.rnk[px] < self.rnk[py]:
                self.par[px] = py
            else:
                self.par[py] = px
                self.rnk[px] += 1

        return False


class Solution1:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """LeetCode 399

        Another lackluster performance. I knew it is union find, but I forgot
        how complex the value update is during union. The main issue is when two
        symbols have already been assigned values, and they need to be unioned,
        what do we do?

        The answer is one of them will serve as the base, and the other has to
        scale. But more than that, all the symbols originally associated with
        the scaled symbol need to be scaled as well. And all of this scaling
        must take place before union.
        
        55 ms, faster than 5.78%
        """
        dsu = DSU()
        for (a, b), v in zip(equations, values):
            dsu.union(a, b, v)
        
        res = []
        for a, b in queries:
            if dsu.find(a) != dsu.find(b) or (dsu.val[a] < 0 or dsu.val[b] < 0):
                res.append(-1.0)
            else:
                res.append(dsu.val[a] / dsu.val[b])
        return res


class DSU2:
    def __init__(self) -> None:
        self.par = {}
        self.val = defaultdict(lambda: 1)

    def find(self, x: int) -> int:
        if x not in self.par:
            self.par[x] = x
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int, v: float) -> None:
        px, py = self.find(x), self.find(y)
        # here is the trick. We always assign py as the parent, or we always
        # consider x in terms of y.
        ratio = v * self.val[y] / self.val[x]
        # Then we update all the values associated with x, in terms of y, before
        # the current union
        for syb, p in self.par.items():
            if p == px:
                self.val[syb] *= ratio
                self.par[syb] = py

class Solution2:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """From the solution one year ago. The trick in union is to always
        designate py as the par, and then update the value of the entire cohort
        associated with px in terms of the value of y.

        44 ms, faster than 31.85%
        """
        dsu = DSU2()
        for (a, b), v in zip(equations, values):
            dsu.union(a, b, v)
        
        res = []
        for a, b in queries:
            if dsu.find(a) != dsu.find(b) or a not in dsu.val or b not in dsu.val:
                res.append(-1.0)
            else:
                res.append(dsu.val[a] / dsu.val[b])
        return res


sol = Solution2()
tests = [
    ([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]], [6.00000,0.50000,-1.00000,1.00000,-1.00000]),
    ([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]], [3.75000,0.40000,5.00000,0.20000]),
    ([["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]], [0.50000,2.00000,-1.00000,-1.00000]),
    ([["a","b"],["e","f"],["b","e"]], [3.4,1.4,2.3], [["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]], [0.29412,10.94800,1.00000,1.00000,-1.00000,-1.00000,0.71429]),
    ([["a","b"],["c","b"],["d","b"],["w","x"],["y","x"],["z","x"],["w","d"]], [2.0,3.0,4.0,5.0,6.0,7.0,8.0], [["a","c"],["b","c"],["a","e"],["a","a"],["x","x"],["a","z"]], [0.66667,0.33333,-1.00000,1.00000,1.00000,0.04464]),
]

for i, (equations, values, queries, ans) in enumerate(tests):
    res = sol.calcEquation(equations, values, queries)
    if all(math.isclose(r, a, rel_tol=1e-3) for r, a in zip(res, ans)):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
