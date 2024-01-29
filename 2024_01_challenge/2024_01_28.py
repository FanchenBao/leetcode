# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter

class Solution1:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        """
        LeetCode 1074

        Spent a bit more than one hour on this, but at least I solved it by
        myself. The idea is to consider submatrices of one row as a 1D array,
        two rows as a 1D array, etc., so that for each multi-row 1D array, we
        can use a simple counter and the current prefix sum of the "1D array"
        to determine whether a submatrix can sum up to the target.

        To facilitate this method, a column-wise prefix sum matrix is created
        ahead of time. And as we go through each cell in the matrix, we go
        through different multi-row 1D array to find each's prefix sum and
        update the counter.

        However, as I skimmed through my solution to this problem before, I
        saw better implementation. So I will have to study that later.

        O(M^2N), 891 ms, faster than 16.53%
        """
        M, N = len(matrix), len(matrix[0])
        psum_cols = [[0] * N for _ in range(M)]
        for j in range(N):
            psum = 0
            for i in range(M):
                psum += matrix[i][j]
                psum_cols[i][j] = psum
        res = 0
        for i in range(M):
            psums = [0] * (i + 1)
            pcounts = [Counter([0]) for _ in range(i + 1)]
            for j in range(N):
                for k in range(i, -1, -1):
                    val = psum_cols[i][j] - (psum_cols[k - 1][j] if k > 0 else 0)
                    psums[k] += val
                    res += pcounts[k][psums[k] - target]
                    pcounts[k][psums[k]] += 1
        return res


class Solution2:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        """
        Exactly the same idea as Solution1, but with simpler implementation.

        O(M^2N), 806 ms, faster than 21.49%
        """
        M, N = len(matrix), len(matrix[0])
        psum_cols = [[0] * N for _ in range(M)]
        for j in range(N):
            psum = 0
            for i in range(M):
                psum += matrix[i][j]
                psum_cols[i][j] = psum
        res = 0
        for i in range(M):
            for k in range(i, -1, -1):
                psum = 0
                pcount = Counter([0])
                for j in range(N):
                    psum += psum_cols[i][j] - (psum_cols[k - 1][j] if k > 0 else 0)
                    res += pcount[psum - target]
                    pcount[psum] += 1
        return res
   


sol = Solution()
tests = [
    ([[0,1,0],[1,1,1],[0,1,0]], 0, 4),
]

for i, (matrix, target, ans) in enumerate(tests):
    res = sol.numSubmatrixSumTarget(matrix, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
