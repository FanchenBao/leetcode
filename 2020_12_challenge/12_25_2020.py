# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class Solution1:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        """Not particularly hard, but it does take some twist and turns to get
        the traversal order correct. The basic idea is that when i and j go
        out of range, there are two situations. The first situation is that
        i and j has just gone out of bound. This is an indication that a change
        in direction is needed. And along with change of direction, we also
        need to reposition the current i and h. The second situation is when
        i and j remains out of bound. Since the direction has changed upon i
        and j going out of bound the first time, the second out of bound
        situation does not require any special attention. We simply follow the
        current direction and just skip the i and j which do not point to any
        cell in the matrix.

        O(N * M), 192 ms, 67% ranking.
        """
        M = len(matrix)
        if not M:
            return []
        N = len(matrix[0])
        if not N:
            return []
        res = []
        i, j = 0, 0
        di, dj = -1, 1
        pre_good = True  # whether the previous i, j values are valid
        while i != M - 1 or j != N - 1:  # we always end on the last element
            if 0 <= i < M and 0 <= j < N:
                res.append(matrix[i][j])
                i += di
                j += dj
                pre_good = True
            elif pre_good:  # current i, j not good but last one is good
                # time to switch direction
                if di < 0:
                    i += 1
                else:
                    j += 1
                di *= -1
                dj *= -1
                pre_good = False
            else:  # current i, j not good and neither is the previous one
                # this means direction has already been changed, just skip
                # the current i, j
                i += di
                j += dj
        res.append(matrix[-1][-1])
        return res


class Solution2:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        """A much better solution. Using the sum of each element's coordinates
        to determine which diagonal it is on, because elements on the same
        diagonal line has the same coordinate sum.

        According to:
        https://leetcode.com/problems/diagonal-traverse/discuss/581868/Easy-Python-NO-DIRECTION-CHECKING
        """
        diags = defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                diags[i + j].append(matrix[i][j])
        res = []
        for n, diag in enumerate(diags.values()):
            res += diag[::-1] if n % 2 == 0 else diag
        return res


sol = Solution2()
tests = [
    ([[1, 2], [3, 4]], [1, 2, 3, 4]),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 4, 7, 5, 3, 6, 8, 9]),
    ([], []),
    ([[]], []),
    ([[1]], [1]),
]

for i, (matrix, ans) in enumerate(tests):
    res = sol.findDiagonalOrder(matrix)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
