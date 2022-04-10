# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        coord_arti = {}
        arti_occ = defaultdict(int)
        for k, arti in enumerate(artifacts):
            for i in range(arti[0], arti[2] + 1):
                for j in range(arti[1], arti[3] + 1):
                    coord_arti[(i, j)] = k
                    arti_occ[k] += 1
        for di, dj in dig:
            if (di, dj) in coord_arti:
                arti_occ[coord_arti[(di, dj)]] -= 1
        return sum(v == 0 for v in arti_occ.values())

        
sol = Solution()
tests = [
    (2, [[0,0,0,0],[0,1,1,1]], [[0,0],[0,1]], 1),
    (2, [[0,0,0,0],[0,1,1,1]], [[0,0],[0,1],[1,1]], 2),
]

for i, (n, artifacts, dig, ans) in enumerate(tests):
    res = sol.digArtifacts(n, artifacts, dig)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
