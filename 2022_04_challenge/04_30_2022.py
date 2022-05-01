# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict
import math


class DSU:
    def __init__(self):
        self.par = {}
        self.val = defaultdict(lambda: 1)

    def find(self, x: str) -> str:
        if x not in self.par:
            self.par[x] = x
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: str, y: str, q: float) -> None:
        # arbitrarily force all nodes in union find to point to py as
        # their new parent. Also, update everyone's value as well
        # according to the new ratio
        px, py = self.find(x), self.find(y)
        ratio = self.val[y] * q / self.val[x]
        for node, par in self.par.items():
            if par == px:
                self.par[node] = py
                self.val[node] *= ratio


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """LeetCode 399

        Very tough problem. It was very tough the last time and equally tough
        this time. In fact, it is even worse this time, because last time at
        least I solved it, albeit using a convoluted solution. This time, I
        knew the solution must be union find, but still I couldn't figure out
        how. Fortunately, by such struggle, I was able to drastically improve
        the union find code compared to a year ago.

        The idea is simple. We create a custom union find, where the par array
        becomes a dict, because the input nodes are no longer integers, but
        string. Also, we can do away with the rank array, because we will
        arbitrarily always pick the parent of the second node in the union
        operation as the parent. The key is to keep another dict that stores
        the values of each node, given that the current parents have value 1.
        This requires computing a ratio that each node that is already in the
        union and has the same parent as the first node in the union operation
        must multiply in order to modify its value.

        When computing the output, we have to check whether the query nodes are
        in union find, AND if they are in union find, whether they have the
        same parent. The latter check is crucial because only nodes that share
        the same parent can have their values divided.

        32 ms, faster than 87.32%
        """
        uf = DSU()
        for (x, y), v in zip(equations, values):
            uf.union(x, y, v)
        res = []
        for x, y in queries:
            if x not in uf.val or y not in uf.val or uf.find(x) != uf.find(y):
                res.append(-1.0)
            else:
                res.append(uf.val[x] / uf.val[y])
        return res


sol = Solution()
tests = [
    ([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]], [6.00000,0.50000,-1.00000,1.00000,-1.00000]),
    ([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]], [3.75000,0.40000,5.00000,0.20000]),
    ([["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]], [0.50000,2.00000,-1.00000,-1.00000]),
    ([["a","b"],["e","f"],["b","e"]], [3.4,1.4,2.3], [["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]], [0.29412,10.94800,1.00000,1.00000,-1.00000,-1.00000,0.71429]),
    ([["a","b"],["c","d"]], [1.0,1.0], [["a","c"],["b","d"],["b","a"],["d","c"]], [-1.00000,-1.00000,1.00000,1.00000]),
]

for i, (equations, values, queries, ans) in enumerate(tests):
    res = sol.calcEquation(equations, values, queries)
    if all(math.isclose(r, a, rel_tol=0.0001) for r, a in zip(res, ans)):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
