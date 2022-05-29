# from pudb import set_trace; set_trace()
from typing import List
from bisect import bisect_right
from collections import defaultdict


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        gs_r = defaultdict(list)
        ws_r = defaultdict(list)
        gs_c = defaultdict(list)
        ws_c = defaultdict(list)
        for r, c in guards:
            gs_r[r].append(c)
            gs_c[c].append(r)
        for row in gs_r.values():
            row.sort()
        for col in gs_c.values():
            col.sort()
        for r, c in walls:
            ws_r[r].append(c)
            ws_c[c].append(r)
        for row in ws_r.values():
            row.sort()
        for col in ws_c.values():
            col.sort()
        res = 0
        for i in range(m):
            for j in range(n):
                if gs_r[i]:
                    a = bisect_right(gs_r[i], j) 
                    if gs_r[i][a - 1] == j:  # (i, j) is a guard
                        continue
                    if not ws_r[i]:  # no wall
                        continue
                    b = bisect_right(ws_r[i], j)
                    if ws_r[i][b - 1] == j:  # (i, j) is a wall
                        continue
                    if a > 0:
                        lg = gs_r[i][a - 1]        
                        c = bisect_right(ws_r[i], lg)
                        if b == c:  # cell can be seen
                            continue
                    if a < len(gs_r[i]):
                        rg = gs_r[i][a] 
                        c = bisect_right(ws_r[i], rg)
                        if b == c:  # cell can be seen
                            continue
                elif ws_r[i]:
                    # (i, j) is a wall
                    if ws_r[i][bisect_right(ws_r[i], j) - 1] == j:
                        continue
                if gs_c[j]:
                    a = bisect_right(gs_c[j], i) 
                    if gs_c[j][a - 1] == i:  # (i, j) is a guard
                        continue
                    if not ws_c[j]:
                        continue
                    b = bisect_right(ws_c[j], i)
                    if ws_c[j][b - 1] == i:  # (i, j) is a wall
                        continue
                    if a > 0:
                        tg = gs_c[j][a - 1]        
                        c = bisect_right(ws_c[j], tg)
                        if b == c:  # cell can be seen
                            continue
                    if a < len(gs_c[j]):
                        bg = gs_c[j][a] 
                        c = bisect_right(ws_c[j], bg)
                        if b == c:  # cell can be seen
                            continue
                elif ws_c[j]:
                    # (i, j) is a wall
                    if ws_c[j][bisect_right(ws_c[j], i) - 1] == i:
                        continue
                res += 1
        return res


sol = Solution()
tests = [
    (4, 6,  [[0,0],[1,1],[2,3]],  [[0,1],[2,2],[1,4]], 7),
    (3, 3, [[1,1]],[[0,1],[1,0],[2,1],[1,2]], 4),
    (4, 3, [[1,0]], [[0,0],[1,2],[0,2],[2,1],[0,1],[2,2]], 2),
]

for i, (m, n, guards, walls, ans) in enumerate(tests):
    res = sol.countUnguarded(m, n, guards, walls)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
