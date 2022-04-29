# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


class Solution1:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """Naive solution does not work.

        TLE
        """
        M, N = len(heights), len(heights[0])
        dp = [[math.inf] * N for _ in range(M)]
        
        def dfs(i: int, j: int, max_effort: int, path) -> None:
            if max_effort >= dp[i][j]:
                return
            dp[i][j] = max_effort
            if i == M - 1 and j == N - 1:
                return
            path.add((i, j))
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < M and 0 <= nj < N and (ni, nj) not in path:
                    dfs(ni, nj, max(max_effort, abs(heights[ni][nj] - heights[i][j])), path)
            path.remove((i, j))

        dfs(0, 0, 0, set())
        return dp[M - 1][N - 1]


class Solution2:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """Convert to a graph. Edge weight is the difference in heights. This
        becomes Dijkstra.

        I did see the hint.

        Two things to note:
        1. we can return immediately when the lower right is reached, because
        according to Dijkstra, each node visited is the best way to reach that
        node.
        2. there is no need to set up a path set that records the nodes visited
        this is because we will not go back to a node visited before unless
        we have a good reason to do so, which is going back reduces the effort.
        """
        M, N = len(heights), len(heights[0])
        dp = [[math.inf] * N for _ in range(M)]
        heap = [(0, 0, 0)]
        while heap:
            d, i, j = heapq.heappop(heap)
            if i == M - 1 and j == N - 1:
                return d  # when a node is visited, it's guaranteed that the effort is minimum
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < M and 0 <= nj < N:
                    cur_d = max(d, abs(heights[ni][nj] - heights[i][j]))
                    if cur_d < dp[ni][nj]:
                        dp[ni][nj] = cur_d
                        heapq.heappush(heap, (cur_d, ni, nj))


class Solution3:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """DFS + binary search

        Key insight is that during DFS, even if we are doing something similar
        to backtracking, we do not un-flag the current node when the dfs call
        ends. This is because if going from the current node cannot reach the
        destination, it is also impossible to go to the destination from the
        current node if it is reached again from some other path.

        3041 ms, faster than 19.29%
        """
        M, N = len(heights), len(heights[0])
        dp = [[math.inf] * N for _ in range(M)]
        
        def dfs(i: int, j: int, thresh: int, path) -> bool:
            if i == M - 1 and j == N - 1:
                return True
            path.add((i, j))
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < M and 0 <= nj < N and (ni, nj) not in path:
                    e = abs(heights[ni][nj] - heights[i][j])
                    if e <= thresh and dfs(ni, nj, thresh, path):
                        return True
            return False

        lo, hi = 0, 1000000
        while lo < hi:
            mid = (lo + hi) // 2
            if dfs(0, 0, mid, set()):
                hi = mid
            else:
                lo = mid + 1
        return lo


sol = Solution3()
tests = [
    ([[1,2,2],[3,8,2],[5,3,5]], 2),
    ([[1,2,3],[3,8,4],[5,3,5]], 1),
    ([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]], 0),
    ([[1,10,6,7,9,10,4,9]], 9),
    ([[10,8],[10,8],[1,2],[10,3],[1,3],[6,3],[5,2]], 6),
]

for i, (heights, ans) in enumerate(tests):
    res = sol.minimumEffortPath(heights)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
