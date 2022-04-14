# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """LeetCode 59

        The analysis itself requires a bit of thinking, but overall not too
        difficult.

        O(N^2), 42 ms, 63.38%
        """
        res = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for v in range(1, n * n + 1):
            res[i][j] = v
            i, j = i + di, j + dj
            if dj == 1 and (j == n or res[i][j]):
                i, j = i + 1, j - 1
                di, dj = 1, 0
            elif di == 1 and (i == n or res[i][j]):
                i, j = i - 1, j - 1
                di, dj = 0, -1
            elif dj == -1 and (j < 0 or res[i][j]):
                i, j = i - 1, j + 1
                di, dj = -1, 0
            elif di == -1 and (i < 0 or res[i][j]):
                i, j = i + 1, j + 1
                di, dj = 0, 1
        return res


class Solution2:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """Better implementation from previous attempts. The key observation
        is that each time we change direction, di and dj follows this relation-
        ship:

        di, dj = dj, -di
        """
        res = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for v in range(1, n * n + 1):
            res[i][j] = v
            ni, nj = i + di, j + dj
            if not 0 <= ni < n or not 0 <= nj < n or res[ni][nj]:
                di, dj = dj, -di  # this is where magic happens
            i, j = i + di, j + dj
        return res


sol = Solution2()
tests = [
    (3, [[1,2,3],[8,9,4],[7,6,5]]),
    (1, [[1]]),
]

for i, (n, ans) in enumerate(tests):
    res = sol.generateMatrix(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
