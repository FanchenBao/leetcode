# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import deque, defaultdict
import heapq


class Solution1:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """TLE.

        This is not a DP problem, because each problem is not completely
        dependent on its subproblem. It also depends on its parent problem.
        """
        m, n = len(heights), len(heights[0])
        h_diffs = [[math.inf] * n for _ in range(m)]
        h_diffs[m - 1][n - 1] = 0
        visited = set()

        def dp(i, j):
            h_ij = math.inf
            visited.add((i, j))
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= m or nj < 0 or nj >= n or (ni, nj) in visited:
                    continue
                cur_h_diff = abs(heights[ni][nj] - heights[i][j])
                visited.add((ni, nj))
                dp(ni, nj)
                h_ij = min(h_ij, max(cur_h_diff, h_diffs[ni][nj]))
                h_diffs[i][j] = min(h_diffs[i][j], h_ij)
                visited.remove((ni, nj))

        dp(0, 0)
        return h_diffs[0][0]


class Solution2:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """I wasn't able to solve this problem by myself. I checked the hints
        and wrote the algo based on it. I had to admit that this was a very
        clever solution. I use BFS to check whether a route exists from start to
        end. Then use binary search to find the min height diff that a route
        can be formed in the matrix.

        O(M*Nlog(max_diff)), about 3000 to 4000 ms, < 17% ranking.
        """
        m, n = len(heights), len(heights[0])

        def exist_route(k: int) -> bool:
            queue = deque([(0, 0)])
            visited = {(0, 0)}
            while queue:
                i, j = queue.popleft()
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if ni < 0 or ni >= m or nj < 0 or nj >= n or (ni, nj) in visited:
                        continue
                    if abs(heights[i][j] - heights[ni][nj]) > k:
                        continue
                    if ni == m - 1 and nj == n - 1:
                        return True
                    queue.append((ni, nj))
                    visited.add((ni, nj))
            return False

        min_h, max_h = heights[0][0], heights[0][0]
        for row in heights:
            min_h = min(min_h, min(row))
            max_h = max(max_h, max(row))
        left, right = 0, max_h - min_h
        while left < right:
            mid = (left + right) // 2
            if exist_route(mid):
                right = mid
            else:
                left = mid + 1
        return left


class Solution3:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """The friking Djikstra!!! I thought about it but didn't go down that
        path. Silly me and lazy me!

        Below is the Djikstra algo. Note that with `node_dists`, we don't need
        to have a `visited` array to check whether a node has been visited
        before, because if a node has not been visited, `node_dists` would show
        that its distance is infinite. If it has been visited, but the current
        path leads to a smaller distance, we will visit it regardless.

        From the point of view of Djikstra, this is indeed a medium question.

        O(MNlog(MN)), 760 ms, 72% ranking.
        """
        m, n = len(heights), len(heights[0])
        node_dists = [[math.inf] * n for _ in range(m)]
        next_nodes = []
        heapq.heappush(next_nodes, (0, 0, 0))  # distance, i, j

        while next_nodes:
            d, i, j = heapq.heappop(next_nodes)
            if i == m - 1 and j == n - 1:
                return d
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    new_dif = max(d, abs(heights[i][j] - heights[ni][nj]))
                    if new_dif < node_dists[ni][nj]:
                        node_dists[ni][nj] = new_dif
                        heapq.heappush(next_nodes, (node_dists[ni][nj], ni, nj))


sol = Solution3()
tests = [
    ([[1, 2, 2], [3, 8, 2], [5, 3, 5]], 2),
    ([[1, 2, 3], [3, 8, 4], [5, 3, 5]], 1),
    ([[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]], 0),
    ([[4, 3, 4, 10, 5, 5, 9, 2], [10, 8, 2, 10, 9, 7, 5, 6], [5, 8, 10, 10, 10, 7, 4, 2], [5, 1, 3, 1, 1, 3, 1, 9], [6, 4, 10, 6, 10, 9, 4, 6]], 5),
]

for i, (heights, ans) in enumerate(tests):
    res = sol.minimumEffortPath(heights)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
