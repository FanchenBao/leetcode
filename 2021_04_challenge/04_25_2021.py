# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """LeetCode 48

        It's not complicated, but it takes quite a toll on my brain cells,
        which were quite mushy to begin with. The intuition is that the rotation
        can be deconstructed as rotation of each layer of the matrix. So we
        perform rotation on the outer most layer, then a layer inward, then
        another layer inward, until we end up with a single cell or no cell at
        all.

        At each layer, we start from the upper left corner, perform swapping
        with its target destination. Since each rotation takes four iterations,
        we can write that out manually. We need to loop through all the values
        on one edge of the outer layer.

        O(MN), where M is the number of rows and N columns. 32 ms, 82% ranking.
        """
        si, sj = 0, 0
        ei, ej = len(matrix) - 1, len(matrix[0]) - 1
        while si < ei and sj < ej:
            for i in range(ej - sj):
                temp = matrix[si][sj + i]
                matrix[si][sj + i] = matrix[ei - i][sj]
                matrix[ei - i][sj] = matrix[ei][ej - i]
                matrix[ei][ej - i] = matrix[si + i][ej]
                matrix[si + i][ej] = temp
            si, sj = si + 1, sj + 1
            ei, ej = ei - 1, ej - 1


sol = Solution()
tests = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
    ([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]], [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]),
    ([[1]], [[1]]),
]

for i, (matrix, ans) in enumerate(tests):
    sol.rotate(matrix)
    if matrix == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {matrix}')
