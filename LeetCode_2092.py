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
        """This is a good problem. It is apparently union-find, but there are
        two twists.

        First, we need to deal with the situation like this

        [[3,1,3],[1,2,2],[0,3,3]] with firstPerson = 3

        The first meeting is between 1 and 2; neither has secret. The second
        meeting is between 3 and 1, so now 1 has secret. However, the meeting
        between 1 and 2 happens earlier. Thus, 2 still does not have secret,
        despite 1 having secret. If we use a naive union-find, where 1 and 2
        are unioned. Then when 1 and 3 are unioned, 2 would've been unioned
        with 3 as well, making him share secret. We must break such tie. Hence
        during iteration of the meeting (in ascending time order), whenever all
        the meetings of the same time have ended, we check to see if any of the
        people involved does not share secret. For such outsider, we must cut
        its tie to any of the union before.

        Second, we want anyone that union with someone else who has zero as
        parent to also have zero as parent. However, since the union is decided
        by the rank of the parent, it is likely the rank of zero is lower than
        the rank of another parent, if the other parent is unioned ahead of
        time. Therefore, we must arbitrarily set the rank of zero maximum,
        thus guaranteeing that whoever unions with some with parent as zero
        also gets zero as parent.

        O(MlogM + (M + N)alpha(N)), where M = len(meetings), and alpha(N) is
        the inverse function of Ackermann function, which describes the time
        complexity of union find with path compression.

        5625 ms, faster than 12.50%

        Time complexity inspired by: https://leetcode.com/problems/find-all-people-with-secret/discuss/1599815/C%2B%2B-Union-Find
        """
        meetings.sort(key=lambda tup: tup[2])
        dsu = DSU(n)
        dsu.union(0, firstPerson)
        pre_t = 0
        outsider = set()
        for x, y, t in meetings:
            if t != pre_t:
                for p in outsider:
                    if dsu.find(p) != 0:
                        # at the end of a specific time, if a person is not
                        # part of the secret, he must be removed of any
                        # connection to any other outsider who might become an
                        # insider later on. This is to avoid such other outsider
                        # becoming an insider pulls the current person into the
                        # secret as well
                        dsu.detach(p)
                outsider = set()
            dsu.union(x, y)
            pre_t = t
            if dsu.find(x):
                outsider.add(x)
            if dsu.find(y):
                outsider.add(y)
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
