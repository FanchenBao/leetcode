# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        """This method always DFS to the biggest neighbor until the current
        cell is the biggest. I think it is faster than brute force, but it is
        kinda brute force as well.

        It's not log time complexity.
        O(MN), 3053 ms, faster than 5.09%
        """
        M, N = len(mat), len(mat[0])
        
        def dfs(i: int, j: int) -> List[int]:
            max_i, max_j = i, j
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < M and 0 <= nj < N and mat[ni][nj] > mat[max_i][max_j]:
                    max_i, max_j = ni, nj
            if (max_i, max_j) == (i, j):
                return [i, j]
            return dfs(max_i, max_j)

        return dfs(0, 0)


class Solution2:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        """This is the most naive O(MN)

        2323 ms, faster than 20.22%
        """
        M, N = len(mat), len(mat[0])
        for i in range(M):
            for j in range(N):
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < M and 0 <= nj < N and mat[ni][nj] > mat[i][j]:
                        break
                else:
                    return [i, j]

class Solution3:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        """This is O(MNlog(N)), because the merge cost is O(MN)
        3547 ms, faster than 5.09%
        """
        M, N = len(mat), len(mat[0])

        def helper(lo: int, hi: int) -> List[int]:
            mid = (lo + hi) // 2
            if hi - lo > 1:
                left = helper(lo, mid)
                if left:
                    return left
                right = helper(mid + 1, hi)
                if right:
                    return right
            # handle the mid col
            for i in range(M):
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ni, nj = i + di, mid + dj
                    if 0 <= ni < M and 0 <= nj < N and mat[ni][nj] > mat[i][mid]:
                        break
                else:
                    return [i, mid]
            # handle the mid + 1 col
            for i in range(M):
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ni, nj = i + di, mid + 1 + dj
                    if 0 <= ni < M and 0 <= nj < N and mat[ni][nj] > mat[i][mid + 1]:
                        break
                else:
                    return [i, mid + 1]
            return []

        return helper(0, N - 1)


class Solution4:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        """This is the binary search method from the official hint.

        It goes like this. We pick out the middle column, and the one column
        on its left and right. Among these three columns, find the max cell.
        If the max cell is in the middle column, we are done.

        If not, we go to the side where the max cell resides. For instance, if
        the max cell is in the column to the left of the middle column, we go
        to the left half of the matrix and repeat the same process, until a
        peak is found.

        This works because we have found a local peak on the left column. If
        this local peak is indeed the true peak, then searching in the left
        half of the matrix will eventually find it. If the local peak is not
        the true peak, that means there must exist another cell with even
        bigger value in the column to the left of the left column (otherwise,
        the local peak would've been the true peak). This can go on and on
        until the final biggest local peak resides in the first column of the
        matrix, which according to the definition, becomes the true peak by
        default.
        """
        M, N = len(mat), len(mat[0])
        lo, hi = 0, N - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            max_i, max_j, max_val = -1, -1, -1
            for i in range(M):
                for j in range(mid - 1, mid + 2):
                    if 0 <= j < N and mat[i][j] > max_val:
                        max_i, max_j, max_val = i, j, mat[i][j]
            if max_j == mid:
                return [max_i, max_j]
            if max_j == mid - 1:
                hi = mid - 1
            else:
                lo = mid + 1


class Solution5:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        """Let's we go row-wise, because the max value can be computed simply by
        max(row).

        Slightly faster: 2645 ms, faster than 14.06%
        """
        M, N = len(mat), len(mat[0])
        lo, hi = 0, M - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            max_mid = max(mat[mid])
            max_mid_up = max(mat[mid - 1]) if mid > 0 else -1
            max_mid_down = max(mat[mid + 1]) if mid < M - 1 else -1
            if max_mid >= max_mid_up and max_mid >= max_mid_down:
                return [mid, mat[mid].index(max_mid)]
            if max_mid_up >= max_mid and max_mid_up >= max_mid_down:
                hi = mid - 1
            elif max_mid_down >= max_mid and max_mid_down >= max_mid_up:
                lo = mid + 1


sol = Solution6()
tests = [
    ([[1,4],[3,2]], [0, 1]),
    ([[10,20,15],[21,30,14],[7,16,32]], [2, 2]),
    ([[1,2,3,4,5,6,7,8],[2,3,4,5,6,7,8,9],[3,4,5,6,7,8,9,10],[4,5,6,7,8,9,10,11]], [3,7]),
    ([[45,35,27,15,29],[38,18,1,49,11],[45,28,22,18,10],[14,49,7,6,25],[7,23,39,17,3]], [1,3])
]

for i, (mat, ans) in enumerate(tests):
    res = sol.findPeakGrid(mat)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
