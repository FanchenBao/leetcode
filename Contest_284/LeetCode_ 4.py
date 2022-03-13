# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict
import math





sol = Solution()
tests = [
    (6, [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]], 0, 1, 5, 9),
    (3, [[0,1,1],[2,1,1]], 0, 1, 2, -1),
]

for i, (n, edges, src1, src2, dest, ans) in enumerate(tests):
    res = sol.minimumWeight(n, edges, src1, src2, dest)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
