# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        """LeetCode 566

        Use the (i * n + j) % c trick to obtain the column index in the new
        matrix from any value in the old matrix.

        O(MN), where M and N are the row and col numbers of mat. 88ms
        65% ranking
        """
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        res = [[0] * c for _ in range(r)]
        ii = 0
        for i in range(m):
            for j in range(n):
                jj = (i * n + j) % c
                res[ii][jj] = mat[i][j]
                if jj == c - 1:
                    ii += 1
        return res


sol = Solution()
tests = [
    ([[1, 2], [3, 4]], 1, 4, [[1, 2, 3, 4]]),
    ([[1, 2], [3, 4]], 2, 4, [[1, 2], [3, 4]]),
]

for i, (mat, r, c, ans) in enumerate(tests):
    res = sol.matrixReshape(mat, r, c)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
