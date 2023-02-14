# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_left, bisect_right
from itertools import accumulate


class Solution1:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        """TLE
        """
        res = [[0] * n for _ in range(n)]
        mat = [[] for _ in range(n)]
        for lab, (i, j, p, q) in enumerate(queries):
            for k in range(i, p + 1):
                mat[k].append((j, 0, lab))
                mat[k].append((q, 1, lab))
        for i, row in enumerate(mat):
            row.sort()
            overlaps = set()
            pre_idx = 0
            for idx, status, lab in row:
                if status == 0:
                    if len(overlaps) > 0:
                        for j in range(pre_idx, idx):
                            res[i][j] = len(overlaps)
                    overlaps.add(lab)
                    pre_idx = idx
                else:
                    for j in range(pre_idx, idx + 1):
                        res[i][j] = len(overlaps)
                    overlaps.remove(lab)
                    pre_idx = idx + 1
        return res


class Solution2:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        """This is the solution after reading the hint. We basically got the
        main idea, but the implementation in Solution 1 was bad. We don't have
        to set up a separate set to include starts and remove ends. All we need
        to do is to add 1 and minus 1 in a prefix matrix. Then we can go through
        the prefix matrix row by row and compute its prefix sum. That is the
        result of query add.

        O(N^2 + NK), where K = len(queries)
        """
        psum = [[0] * (n + 1) for _ in range(n)]
        for i, j, p, q in queries:
            for k in range(i, p + 1):
                psum[k][j] += 1
                psum[k][q + 1] -= 1
        return [list(accumulate(row))[:-1] for row in psum]


sol = Solution2()
tests = [
    (3, [[1,1,2,2],[0,0,1,1]], [[1,1,0],[1,2,1],[0,1,1]]),
    (2, [[0,0,1,1]], [[1,1],[1,1]]),
]

for i, (n, queries, ans) in enumerate(tests):
    res = sol.rangeAddQueries(n, queries)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
