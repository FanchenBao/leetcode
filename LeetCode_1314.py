# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import accumulate


class Solution:
    def produce(self, mat: List[List[int]]) -> List[List[int]]:
        M, N = len(mat), len(mat[0])
        presum2d = [list(accumulate(mat[0]))]
        for i in range(1, M):
            presum2d.append(list(accumulate(mat[i])))
            for j in range(N):
                presum2d[i][j] += presum2d[i - 1][j]
        return presum2d

    def query(self, tl_i: int, tl_j: int, br_i: int, br_j: int, presum2d: List[List[int]]) -> int:
        M, N = len(presum2d), len(presum2d[0])
        base = presum2d[br_i][br_j]
        rem_l = presum2d[br_i][tl_j - 1] * int(tl_j > 0)
        rem_t = presum2d[tl_i - 1][br_j] * int(tl_i > 0)
        add_d = presum2d[tl_i - 1][tl_j - 1] * int(tl_i > 0) * int(tl_j > 0)
        return base - rem_l - rem_t + add_d

    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        """Nothing special, just a glorified practice of 2D prefix sum.

        O(MN), 122 ms, faster than 85.44% 
        """
        M, N = len(mat), len(mat[0])
        presum2d = self.produce(mat)
        res = [[0] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                res[i][j] = self.query(
                    max(i - k, 0),
                    max(j - k, 0),
                    min(i + k, M - 1),
                    min(j + k, N - 1),
                    presum2d,
                )
        return res


sol = Solution()
tests = [
    ([[1,2,3],[4,5,6],[7,8,9]], 1, [[12,21,16],[27,45,33],[24,39,28]]),
    ([[1,2,3],[4,5,6],[7,8,9]], 2, [[45,45,45],[45,45,45],[45,45,45]]),
]

for i, (mat, k, ans) in enumerate(tests):
    res = sol.matrixBlockSum(mat, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
