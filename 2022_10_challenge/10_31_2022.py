# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import deque


class Solution1:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """LeetCode 766

        Technically, I think this only requires loading one row into memory at
        a time, on condition that we can query matrix content directly from
        disk.

        O(MN), 201 ms, faster than 35.74%
        """
        M, N = len(matrix), len(matrix[0])
        row = matrix[0][:-1]
        for i in range(1, M):
            for j in range(1, N):
                if matrix[i][j] != row[j - 1]:
                    return False
            row = matrix[i][:-1]
        return True


class Solution2:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """Traditional solution, compare to top left neighbor
        """
        return all(i == 0 or j == 0 or matrix[i][j] == matrix[i - 1][j - 1] for i in range(len(matrix)) for j in range(len(matrix[0])))


class Solution3:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """This is from the response in the official solution.

        https://leetcode.com/problems/toeplitz-matrix/solution/1665273

        It's the same idea as Solution1, but does it in a nicer way.
        """
        M, N = len(matrix), len(matrix[0])
        row = deque(matrix[0])
        for i in range(1, M):
            row.pop()  # previou row's last element doesn't need to be compared
            row.appendleft(matrix[i][0])  # current row's first element doesn't need to be compared
            if any(matrix[i][j] != row[j] for j in range(1, N)):
                return False
        return True


sol = Solution3()
tests = [
    ([[1,2,3,4],[5,1,2,3],[9,5,1,2]], True),
    ([[1,2],[2,2]], False)
]

for i, (matrix, ans) in enumerate(tests):
    res = sol.isToeplitzMatrix(matrix)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
