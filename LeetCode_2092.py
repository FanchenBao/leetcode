# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class DSU:
    def __init__(self, N: int):
        self.par = list(range(N))
        self.rnk = [0] * N
        # zero must be the ultimate parent, such that whoever unions with zero,
        # its parent will be zero, regardless of when the union happens
        self.rnk[0] = math.inf

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> bool:
        x_par, y_par = self.find(x), self.find(y)
        if x_par == y_par:
            return False
        if self.rnk[x_par] > self.rnk[y_par]:
            self.par[y_par] = x_par
        elif self.rnk[x_par] < self.rnk[y_par]:
            self.par[x_par] = y_par
        else:
            self.rnk[x_par] += 1
            self.par[y_par] = x_par
        return True

    def detach(self, x: int) -> None:
        """Detach x from any group it might have been associated with."""
        self.par[x] = x
        self.rnk[x] = 0


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda tup: tup[2])
        dsu = DSU(n)
        dsu.union(0, firstPerson)
        # no_secrets = {}  # {person without secret: most recent meeting time}
        pre_t = 0
        people = set()
        for x, y, t in meetings:
            if t != pre_t:
                for p in people:
                    if dsu.find(p) != 0:
                        # at the end of a specific time, if a person is not
                        # part of the secret, he must be removed of any
                        # connection to any other people who might become an
                        # insider later on. This is to avoid such other people
                        # becoming an insider pulls the current person into the
                        # secret as well
                        dsu.detach(p)
                people = set()
            dsu.union(x, y)
            pre_t = t
            if dsu.find(x):
                people.add(x)
            if dsu.find(y):
                people.add(y)
        return [i for i in range(n) if dsu.find(i) == 0]


sol = Solution()
tests = [
    (6, [[1,2,5],[2,3,8],[1,5,10]], 1, [0,1,2,3,5]),
    (4, [[3,1,3],[1,2,2],[0,3,3]], 3, [0,1,3]),
    (5, [[3,4,2],[1,2,1],[2,3,1]], 1, [0,1,2,3,4]),
    (6, [[0,2,1],[1,3,1],[4,5,1]], 1, [0,1,2,3]),
    (6, [[0,2,1],[1,3,1],[4,5,1],[1,4,1]], 1, [0,1,2,3,4,5]),
    (5, [[1,4,3],[0,4,3]], 3, [0,1,3,4]),
    (4, [[1,2,1],[0,3,1],[2,0,1]], 3, [0,1,2,3])
]

for i, (n, meetings, firstPerson, ans) in enumerate(tests):
    res = sol.findAllPeople(n, meetings, firstPerson)
    res.sort()
    ans.sort()
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
