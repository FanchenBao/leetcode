# from pudb import set_trace; set_trace()
from typing import List
import heapq
from collections import defaultdict


class Solution:

    def helper(self, mat: List[List[int]], i: int, j: int) -> None:
        M, N = len(mat), len(mat[0])
        tmp = []
        ii, jj = i, j
        while ii < M and jj < N:
            tmp.append(mat[ii][jj])
            ii += 1
            jj += 1
        tmp.sort(reverse=True)
        ii, jj = i, j
        while ii < M and jj < N:
            mat[ii][jj] = tmp.pop()
            ii += 1
            jj += 1

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        """LeetCode 1329

        We handle the first row. For each cell in the first row, we can extract
        its diagonal, sort it, and put it back. The extraction is simply go
        through mat[i][j] and do i++ and j++.

        Then we handle the first column except the top left corner.

        O(MNlog(?)), 113 ms, faster than 71.30%
        """
        M, N = len(mat), len(mat[0])
        for j in range(N):
            self.helper(mat, 0, j)
        for i in range(1, M):
            self.helper(mat, i, 0)
        return mat


class Solution2:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        """This is from the solution back in Jan, 2021. It uses the fact that
        all cells in a diagonal has the same i - j. Therefore, we can put all
        values in a diagonal in a hashmap by going through the matrix row by
        row, no special order is needed. Then we sort them. Finally add them
        back to the matrix.

        O(MNlog(M + N)) We use heap to simplify the sorting process.
        159 ms, faster than 30.22%
        """
        hashmap = defaultdict(list)
        for i, row in enumerate(mat):
            for j, v in enumerate(row):
                heapq.heappush(hashmap[i - j], v)
        for i, row in enumerate(mat):
            for j, v in enumerate(row):
                mat[i][j] = heapq.heappop(hashmap[i - j])
        return mat


sol = Solution2()
tests = [
    ([[3,3,1,1],[2,2,1,2],[1,1,1,2]], [[1,1,1,1],[1,2,2,2],[1,2,3,3]]),
    ([[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]], [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]),
]

for i, (mat, ans) in enumerate(tests):
    res = sol.diagonalSort(mat)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
