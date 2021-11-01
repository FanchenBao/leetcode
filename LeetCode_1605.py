# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        """TLE, passed 52/84 test cases
        """
        M, N = len(rowSum), len(colSum)
        res = [[-1] * N for _ in range(M)]

        def dfs(i: int, j: int) -> int:
            if j == N - 1:
                if rowSum[i] > colSum[j]:
                    return False
                res[i][j] = rowSum[i]
            if i == M - 1:
                if colSum[j] > rowSum[i]:
                    return False
                if res[i][j] >= 0:  # the last cell
                    return colSum[j] == res[i][j]
                res[i][j] = colSum[j]
            if res[i][j] < 0:
                res[i][j] = min(rowSum[i], colSum[j]) // 2
            rowSum[i] -= res[i][j]
            colSum[j] -= res[i][j]
            while True:
                if (j < N - 1 and dfs(i, j + 1)) or (j == N - 1 and dfs(i + 1, 0)):
                    return True
                pre = res[i][j]
                rowSum[i] += pre
                colSum[j] += pre
                # need to find the mid point between pre + 1 and min(rowSum, colSum)
                # pre + 1 is important, because without it, we will never
                # increment towards min(rowSum, colSum)
                res[i][j] = (pre + 1 + min(rowSum[i], colSum[j])) // 2
                if res[i][j] > pre:
                    rowSum[i] -= res[i][j]
                    colSum[j] -= res[i][j]
                else:
                    res[i][j] = -1
                    return False

        dfs(0, 0)
        return res


class Solution2:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        """I did check the hint, but it was the same idea as I had previously.
        Previously, I was thinking about going with the smallest row or col sum
        first. But later, I decided to not follow through, because perhaps not
        checking the min would save us some runtime. Unfortunately, it did not
        work. Thus, with the confirmation from the hint, I went back to checking
        the min row or col sum first. I did not use priority queue for this,
        because there is a need to update elements in the priority queue. It is
        not impossible, but my current implementation of that requires the
        creation of a custome object to handle this. I don't like it. Thus, I
        simply go through the entire rowSum and colSum to find the min. Since
        the maximum length of these two arrays is 500. O(N) to find min might
        be tolerable.

        After the min is determined, I simply throw the min to the corresponding
        first empty spot in the row or col. This leaves the remaining row or
        col 0. If this scheme doesn't work, we will backtrack and try another
        spot to throw in the min. I don't have a full proof, but I think give
        that a solution must exists, we can always manipulate the solution in
        such away that some row or col can be rentered all zero except for one
        of them.

        O(M^2N^2), 1132 ms, 52% ranking.
        """
        M, N = len(rowSum), len(colSum)
        res = [[0] * N for _ in range(M)]

        def dfs() -> bool:
            i, minr = -1, math.inf
            for ri, rs in enumerate(rowSum):
                if 0 < rs < minr:
                    minr = rs
                    i = ri
            j, minc = -1, math.inf
            for cj, cs in enumerate(colSum):
                if 0 < cs < minc:
                    minc = cs
                    j = cj
            if i < 0 and j < 0:
                return True
            if minr < minc:  # next to fill is row
                for cj in range(N):
                    if res[i][cj] == 0 and colSum[cj] >= minr:
                        res[i][cj] = minr
                        colSum[cj] -= minr
                        rowSum[i] -= minr
                        if dfs():
                            return True
                        res[i][cj] = 0
                        colSum[cj] += minr
                        rowSum[i] += minr
            else:  # next to fill is col
                for ri in range(M):
                    if res[ri][j] == 0 and rowSum[ri] >= minc:
                        res[ri][j] = minc
                        colSum[j] -= minc
                        rowSum[ri] -= minc
                        if dfs():
                            return True
                        res[ri][j] = 0
                        colSum[j] += minc
                        rowSum[ri] += minc
            return False

        dfs()
        return res


class Solution3:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        """From lee215:

        https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/discuss/876845/JavaC%2B%2BPython-Easy-and-Concise-with-Prove

        I don't like lee215's proof. Here is my understanding. We can pick the
        smallest of rowSum[i] and colSum[j] for each res[i][j], because after
        the pick, we also decrement the same valeu from rowSum[i] and colSum[j].
        This means, sum(rowSum) == sum(colSum) is preserved after each
        operation. Then after M * N - 1 operation, which means we are now at
        res[M - 1][N - 1], sum(rowSum) == sum(colSum) still holds. Since we are
        at the end, the only rowSum and colSum that might not be 0 are
        rowSum[M - 1] and colSum[N - 1]. Thus, we can see that rowSum[M - 1] ==
        colSum[N - 1]. In other words, we can pick rowSum[M - 1] (or colSum[N - 1])
        and the matrix will be solved.

        Very smart greedy.
        """
        M, N = len(rowSum), len(colSum)
        res = [[0] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                res[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= res[i][j]
                colSum[j] -= res[i][j]
        return res


sol = Solution3()
tests = [
    ([3, 8], [4, 7]),
    ([5, 7, 10], [8, 6, 8]),
    ([14, 9], [6, 9, 8]),
    ([1, 0], [1]),
    ([0], [0]),
    ([4,12,10,1,0],[1,0,3,16,7]),
    ([52,6,154,31,63,174,21,133,38,76,115,103,121,128,201,229,230,125,172,121,12,1822,231,47],[44,197,129,134,189,211,161,220,12,53,58,115,213,78,232,157,201,214,108,194,197,179,80,40,47,168,147,176,58,212,181]),
]

for i, (rowSum, colSum) in enumerate(tests):
    ans_row_sum = rowSum[:]
    ans_col_sum = colSum[:]
    res = sol.restoreMatrix(rowSum, colSum)
    res_row_sum = [sum(row) for row in res]
    res_col_sum = [sum(col) for col in zip(*res)]
    if res_row_sum == ans_row_sum and res_col_sum == ans_col_sum:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Res: {res}')
