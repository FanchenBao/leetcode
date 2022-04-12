# from pudb import set_trace; set_trace()
from typing import List
from itertools import chain


class Solution1:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """LeetCode 1260

        Flatten and start from the last kth element does the trick.

        O(MN), 228 ms, 55% ranking
        """
        M, N = len(grid), len(grid[0])
        flatten = list(chain(*grid))
        idx = (M * N - k) % (M * N)
        res = [[0] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                res[i][j] = flatten[idx]
                idx = (idx + 1) % (M * N)
        return res


class Solution2:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """Without flatten

        Same runtime as solution1, but much faster. 155 ms, 97.31%
        """
        M, N = len(grid), len(grid[0])
        res = [[0] * N for _ in range(M)]
        p, q = divmod(k, N)
        p, q = (M - p, 0) if q == 0 else (M - p - 1, N - q)
        p = p % M
        for i in range(M):
            for j in range(N):
                res[i][j] = grid[p][q]
                q = (q + 1) % N
                if q == 0:
                    p = (p + 1) % M
        return res
        

sol = Solution2()
tests = [
    ([[1,2,3],[4,5,6],[7,8,9]], 1, [[9,1,2],[3,4,5],[6,7,8]]),
    ([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], 4, [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]),
    ([[1]], 100, [[1]]),
]

for i, (grid, k, ans) in enumerate(tests):
    res = sol.shiftGrid(grid, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
