# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class DSU:
    def __init__(self, N):
        self.rnk = [0] * N
        self.par = list(range(N))

    def find(self, x) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y) -> bool:
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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        """LeetCode 1202

        I solved this problem two years ago, but I don't remember why I did it.
        Anyway, I do remember using Union Find to solve this problem, because
        we can convert the letter swapping to forming and edge between two
        indices. Another insight is that once several indices are combined into
        one graph, then we can make any letter within this graph appear
        anywhere. This means, all we need to do is to find the graphs described
        by the pairs. Within each graph, we can easily sort the letters.

        O((E + V)a(V) + VlogV), 734 ms, faster than 85.32%
        """
        N = len(s)
        uf = DSU(N)
        for a, b in pairs:
            uf.union(a, b)
        for i in range(N):
            uf.find(i)
        gs = defaultdict(list)
        for i, p in enumerate(uf.par):
            gs[p].append(s[i])
        for g in gs.values():
            g.sort(reverse=True)
        return ''.join(gs[uf.find(i)].pop() for i in range(N))



sol = Solution()
tests = [
    ("dcab", [[0,3],[1,2]], 'bacd'),
    ("dcab", [[0,3],[1,2],[0,2]], 'abcd'),
    ("cba", [[0,1],[1,2]], 'abc'),
]

for i, (s, pairs, ans) in enumerate(tests):
    res = sol.smallestStringWithSwaps(s, pairs)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
