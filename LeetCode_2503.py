# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        """First of all, sort queries from small to large. Then as we traverse
        the grid with each increasing query, the next query can always start
        from the end cells of the previous query. Thus, we need to keep track
        of the end cells.
        
        Next, use a heap to keep track of the end cells, such that each time
        we only try traversing from the cell with the smallest value. If for
        some query, the smallest available cell is still too big, we can skip
        it. The point is the total number of cells visited so far.

        O(MNlog(MN))
        Each cell is only visted once. The log part is priority queue.

        3513 ms, faster than 33.92%
        """
        qq = sorted([(q, i) for i, q in enumerate(queries)])
        M, N = len(grid), len(grid[0])
        visited = set()
        heap = [[grid[0][0], 0, 0]]

        def dfs(i: int, j: int, q: int) -> None:
            if (i, j) in visited:
                return
            if grid[i][j] >= q:
                heapq.heappush(heap, [grid[i][j], i, j])
                return
            visited.add((i, j))
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < M and 0 <= nj < N:
                    dfs(ni, nj, q)

        mix_res = []
        for q, _ in qq:
            while heap and heap[0][0] < q:
                _, a, b = heapq.heappop(heap)
                dfs(a, b, q)
            mix_res.append(len(visited))
        res = [0] * len(queries)
        for (_, i), r in zip(qq, mix_res):
            res[i] = r
        return res


sol = Solution()
tests = [
    ([[1,2,3],[2,5,7],[3,5,1]], [5,6,2], [5, 8, 1]),
    ([[5,2,1],[1,1,2]], [3], [0]),
]

for i, (grid, queries, ans) in enumerate(tests):
    res = sol.maxPoints(grid, queries)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
