# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        LeetCode 48
        Do not return anything, modify matrix in-place instead.

        It is not difficult but requires some ingenuity to figure out how the
        rotation is marked along each layer of the matrix.

        O(N^2), 46 ms, faster than 73.91% 
        """
        N = len(matrix)
        for i in range((N + 1) // 2):
            for j in range(i, N - i - 1):
                (
                    matrix[i][j],
                    matrix[j][N - i - 1],
                    matrix[N - i - 1][N - j - 1],
                    matrix[N - j - 1][i],
                ) = (
                    matrix[N - j - 1][i],
                    matrix[i][j],
                    matrix[j][N - i - 1],
                    matrix[N - i - 1][N - j - 1],
                )


sol = Solution()
tests = [
    ([[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]]),
    ([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]], [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]),
]

for i, (matrix, ans) in enumerate(tests):
    sol.rotate(matrix)
    if matrix == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {matrix}')
