# from pudb import set_trace; set_trace()
from typing import List
import math


class DSU:
    def __init__(self, N: int) -> None:
        self.par = list(range(N))
        self.rnk = [0] * N

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rnk[px] > self.rnk[py]:
                self.par[py] = px
            elif self.rnk[px] < self.rnk[py]:
                self.par[px] = py
            else:
                self.par[py] = px
                self.rnk[px] += 1
            return True
        return False


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """LeetCode 1697 (Fail)

        Once the secret sauce is revealed, it's not that difficult. This is not
        the first time that I have seen this thought process. To know whether
        there is a path between two nodes, we create the graph using the edges
        allowed at the moment. Then with union-find, it is very easy to check
        whether the target nodes are connected. We slowly build up the graph
        with ever larger edges, but each time the edges are always within the
        limit, which means for whatever graph built, all the edges are okay to
        use.

        O(ElogE + QlogQ + (E + Q) * union + n), 1903 ms, faster than 80.50% 
        """
        edgeList.sort(key=lambda tup: tup[2])
        dsu = DSU(n)
        i = 0
        res = [None] * len(queries)
        for p, q, lim, j in sorted([(p, q, l, k) for k, (p, q, l) in enumerate(queries)], key=lambda tup: tup[2]):
            while i < len(edgeList) and edgeList[i][2] < lim:
                dsu.union(edgeList[i][0], edgeList[i][1])
                i += 1
            res[j] = dsu.find(p) == dsu.find(q)
        return res



# sol = Solution()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
