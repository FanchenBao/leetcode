# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_left, bisect_right


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
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


sol = Solution()
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
