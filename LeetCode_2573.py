# from pudb import set_trace; set_trace()
from typing import List
import math
import string
from collections import defaultdict


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
    def findTheString(self, lcp: List[List[int]]) -> str:
        """The hint helps a lot. It points to the direction of union find. We
        first use union find to identify which positions share the same letter.

        Then we can create the string, from left to right, filling all the
        positions that share the same letter the smallest letter available at
        the moment.

        Then we recreat the value at each position of lcp and compare it with
        the corresponding value in lcp to check whether lcp has it right.

        Three tricks:

        1. the lcp matrix needs to be traversed diagonally from bottom right to
        top left, because this way we can obtain all the information either for
        union find or for recreating lcp in O(N^2) time. If we traverse it row
        by row, it will take O(N^3).

        2. When filling the letter, make sure to check whether the letter has
        exceeded the lower case English letters.

        3. When checking lcp, make sure to also check whether the target cell
        in lcp and its mirrored cell share the same value as desired.

        O(N^2 * union-find), 2339 ms, faster than 22.74%
        """
        N = len(lcp)

        # union-find to identify which positions share the same letter
        dsu = DSU(N)
        for k in range(1, N):
            for i in range(N - k - 1, -1, -1):
                if lcp[i][i + k]:
                    dsu.union(i, i + k)

        # fill the positions that share the same letter. We go from left to
        # right and gradually increase the letter order
        res = [''] * N
        le = 97  # we start wit 'a', and le cannot be larger than 122
        for i in range(N):
            p = dsu.find(i)
            if not res[p]:
                if le > 122:  # impossible case, because we go beyond "z"
                    return ''
                res[p] = chr(le)
                le += 1
            res[i] = res[p]

        # recreate lcp and check with the original lcp
        for k in range(N):
            acc = 0
            for i in range(N - k - 1, -1, -1):
                j = i + k
                acc = 0 if res[i] != res[j] else acc + 1
                if acc != lcp[i][j] or acc != lcp[j][i]:
                    return ''
        return ''.join(res)

        




sol = Solution()
tests = [
    ([[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]], 'abab'),
    ([[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]], 'aaaa'),
    ([[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]], ''),
    ([[2,0],[1,1]], ''),
    ([[2,2],[2,1]], ''),
    ([[4,1,1,1],[1,3,1,1],[1,1,2,1],[1,1,1,1]], ''),
    ([[8,0,0,0,0,1,2,0],[0,7,0,1,1,0,0,1],[0,0,6,0,0,0,0,0],[0,1,0,5,1,0,0,1],[0,1,0,1,4,0,0,1],[1,0,0,0,0,3,1,0],[2,0,0,0,0,1,2,0],[0,1,0,1,1,0,0,1]], "abcbbaab"),
    ([[14,2,1,0,0,0,1,0,0,0,2,1,0,0],[2,13,1,0,0,0,1,0,0,0,4,1,0,0],[1,1,12,0,0,0,1,0,0,0,1,3,0,0],[0,0,0,11,1,0,0,0,2,1,0,0,2,1],[0,0,0,1,10,0,0,0,1,1,0,0,1,1],[0,0,0,0,0,9,0,1,0,0,0,0,0,0],[1,1,1,0,0,0,8,0,0,0,1,1,0,0],[0,0,0,0,0,1,0,7,0,0,0,0,0,0],[0,0,0,2,1,0,0,0,6,1,0,0,2,1],[0,0,0,1,1,0,0,0,1,5,0,0,1,1],[2,4,1,0,0,0,1,0,0,0,4,1,0,0],[1,1,3,0,0,0,1,0,0,0,1,3,0,0],[0,0,0,2,1,0,0,0,2,1,0,0,2,1],[0,0,0,1,1,0,0,0,1,1,0,0,1,1]], "aaabbcacbbaabb"),
    ([[27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,26,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,23,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,22,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,21,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,20,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,19,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,18,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,17,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,16,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,15,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,14,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,13,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,12,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]], ''),
]

for i, (lcp, ans) in enumerate(tests):
    res = sol.findTheString(lcp)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
