# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """LeetCode 542

        We treat the matrix as a graph. Then, we perform dfs to visit each
        cell and determine the distance for each cell. For a cell at position i
        and j, if mat[i][j] == 0, then res[i][j] = 0. If mat[i][j] == 1, we have
        two scenarios. First, this one is adjacent to some 0. Then we are sure
        that res[i][j] = 1. Otherwise, we are not sure and have to obtain the
        distance from the distance nearby. The trick is to always check the
        surroundings of a one such that if this one is adjacent to a zero, its
        distance can be quickly determined.

        We also make sure each cell is visited once. Thus the runtime is O(MN)

        1104 ms. 10% ranking.
        """
        m, n = len(mat), len(mat[0])
        res = [[-1] * n for _ in range(m)]

        def dfs(i: int, j: int) -> None:
            res[i][j] = math.inf if mat[i][j] else 0
            # preliminary round to get distance for the ones that are adjacent
            # to zeros
            for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    if res[ni][nj] >= 0:
                        res[i][j] = min(res[i][j], res[ni][nj] + 1)
            for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    if res[ni][nj] < 0:
                        dfs(ni, nj)
                    res[i][j] = min(res[i][j], res[ni][nj] + 1)
            return

        dfs(0, 0)
        return res


class Solution2:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """We can consider this as a bottom up solution. We notice that the
        result must not be smaller than mat. So we can do this in place.

        First round of traversal, we identify all the cells that are uncertain.
        An uncertain cell is a one that is surrounded by other ones. We record
        all the cells that are uncertain after the first round.

        Then we do the second session, where we know the min possible distance
        for each round. For instance, the first round of the second session, the
        min distance possible is 2. Thus, if an uncertain cell from the previous
        round scores a 2 in the current round, we are certain that it is the
        min distance that this cell can get. Therefore, we don't have to
        consider this cell anymore. We go through the uncertain list, eliminate
        those that are certain, until the uncertain list is exhausted.

        O(MN), but without recursion, it runs 472 ms, 99% ranking.
        """
        uncertains = []
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n and mat[ni][nj] == 0:
                            break
                    else:
                        mat[i][j] = math.inf
                        uncertains.append((i, j))
        min_possible = 2  # this is the trick!!
        while uncertains:
            temp = []
            for i, j in uncertains:
                for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        mat[i][j] = min(mat[i][j], mat[ni][nj] + 1)
                if mat[i][j] > min_possible:
                    temp.append((i, j))
            uncertains = temp
            min_possible += 1
        return mat


class Solution3:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """Official solution. BFS

        https://leetcode.com/problems/01-matrix/solution/
        """
        m, n = len(mat), len(mat[0])
        queue = []
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    mat[i][j] = math.inf
                else:
                    queue.append((i, j))
        while queue:
            temp = []
            for i, j in queue:
                for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and mat[ni][nj] > mat[i][j] + 1:
                        mat[ni][nj] = mat[i][j] + 1
                        temp.append((ni, nj))
            queue = temp
        return mat



class Solution4:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """Official solution. DP

        https://leetcode.com/problems/01-matrix/solution/
        """
        m, n = len(mat), len(mat[0])
        # first pass. Left to right, top to bottom
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    mat[i][j] = math.inf  # trick. Initialize all ones to inf
                    if i > 0:
                        mat[i][j] = min(mat[i][j], mat[i - 1][j] + 1)
                    if j > 0:
                        mat[i][j] = min(mat[i][j], mat[i][j - 1] + 1)
        # Second pass. Right to left, bottom to top
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j]:
                    if i < m - 1:
                        mat[i][j] = min(mat[i][j], mat[i + 1][j] + 1)
                    if j < n - 1:
                        mat[i][j] = min(mat[i][j], mat[i][j + 1] + 1)
        return mat


sol = Solution4()
tests = [
    ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
    ([[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[0, 0, 0], [0, 1, 0], [1, 2, 1]]),
    ([[0, 1, 1], [1, 1, 1]], [[0, 1, 2], [1, 2, 3]]),
]

for i, (mat, ans) in enumerate(tests):
    res = sol.updateMatrix(mat)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
