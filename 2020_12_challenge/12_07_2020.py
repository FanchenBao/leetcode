# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def dirs(self, di, dj):
        if di == 0 and dj == 1:  # from going right to going down
            return 1, 0
        elif di == 1 and dj == 0:  # from going down to going left
            return 0, -1
        elif di == 0 and dj == -1:  # from going left to going up
            return -1, 0
        elif di == -1 and dj == 0:  # from going up to going right
            return 0, 1

    def generateMatrix(self, n: int) -> List[List[int]]:
        """Naive approach. Just follow the spiral and change direction when
        we go out of bound or hit a cell that has already been populated.

        O(N^2), 28 ms, 84% ranking.
        """
        res = [[0] * n for _ in range(n)]
        i, j = 0, -1
        di, dj = 0, 1
        num = 1
        while num <= n * n:
            i += di
            j += dj
            if 0 <= i < n and 0 <= j < n:
                if not res[i][j]:
                    res[i][j] = num
                else:
                    i, j, di, dj = i - di, j - dj, *self.dirs(di, dj)
                    continue
            else:
                i, j, di, dj = i - di, j - dj, *self.dirs(di, dj)
                continue
            num += 1
        return res


class Solution2:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """Same idea but much better implementation. Refer to:
        https://leetcode.com/problems/spiral-matrix-ii/discuss/22282/4-9-lines-Python-solutions

        O(N^2), 40 ms, 7% ranking.
        """
        res = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for num in range(n * n):
            res[i][j] = num + 1
            if res[(i + di) % n][(j + dj) % n]:  # need to change dir
                di, dj = dj, -di
            i += di
            j += dj
        return res


sol = Solution2()
tests = [
    (3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]]),
    (1, [[1]]),
]

for i, (n, ans) in enumerate(tests):
    res = sol.generateMatrix(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
