# from pudb import set_trace; set_trace()
from typing import List
import heapq
from collections import defaultdict


class Solution1:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        """This must be an easy question. Straightforward solution with no
        tricks or turns. Iterate through the diagonals, sort them and put the
        sorted values back in the matrix.

        O(MN + (M + N) * min(M, N) * log(min(M, N))) = O(MN + MNlog(min(M, N)))
        = O(MNlog(min(M, N))), 84 ms, 74% ranking.
        """
        m, n = len(mat), len(mat[0])
        # start with first column
        for k in range(m - 1, -1, -1):
            i, j, diag = k, 0, []
            while i < m and j < n:
                diag.append(mat[i][j])
                i += 1
                j += 1
            diag.sort()
            while diag:
                i -= 1
                j -= 1
                mat[i][j] = diag.pop()
        # start with first row, except the top left corner
        for k in range(1, n):
            i, j, diag = 0, k, []
            while i < m and j < n:
                diag.append(mat[i][j])
                i += 1
                j += 1
            diag.sort()
            while diag:
                i -= 1
                j -= 1
                mat[i][j] = diag.pop()
        return mat


class Solution2:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        """The heap + hashmap solution. I have encountered this property of
        matrix diagonal before: all elements on a diagonal has the same i - j.
        But as you know, I am quite forgetful, so I wasn't able to recall this
        convenient property.
        """
        diags = defaultdict(list)
        for i, row in enumerate(mat):
            for j, r in enumerate(row):
                heapq.heappush(diags[i - j], r)
        for i, row in enumerate(mat):
            for j, r in enumerate(row):
                mat[i][j] = heapq.heappop(diags[i - j])
        return mat


class Solution3:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        """The numpy solution.

        I wasn't able to come up with the looping scheme, so have to resort to
        Mr. Pochmann for help:
        https://leetcode.com/problems/sort-the-matrix-diagonally/discuss/490049/NumPy-solution
        """
        A = np.array(mat)
        m, n = A.shape
        for i in range(-m + 1, n):
            np.fill_diagonal(
                # this line is where all the magic is. You will have to draw
                # out a matrix and walk through the algorithm yourself to see
                # what it means.
                A[max(-i, 0):, max(i, 0):],
                np.sort(A.diagonal(i))
            )
        return A


sol = Solution2()
tests = [
    ([[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]], [[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]]),
]

for i, (mat, ans) in enumerate(tests):
    res = sol.diagonalSort(mat)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
