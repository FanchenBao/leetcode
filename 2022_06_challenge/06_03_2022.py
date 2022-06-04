# from pudb import set_trace; set_trace()
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        """LeetCode 304

        This is a pretty standard solution of 2D prefix sum.

        O(MN), 1856 ms, faster than 66.42%
        """
        self.mat = matrix
        self.M, self.N = len(self.mat), len(self.mat[0])
        self.prep()
    
    def prep(self) -> None:
        for i, row in enumerate(self.mat):
            for j in range(1, self.N):
                row[j] += row[j - 1]
            if i > 0:
                for j in range(self.N):
                    row[j] += self.mat[i - 1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a = self.mat[row1 - 1][col2] if row1 - 1 >= 0 else 0
        b = self.mat[row2][col1 - 1] if col1 - 1 >= 0 else 0
        c = self.mat[row1 - 1][col1 - 1] if row1 - 1 >= 0 and col1 - 1 >= 0 else 0
        return self.mat[row2][col2] - a - b + c


sol = Solution()
tests = [
    ([4,2,1,3], [[1,2],[2,3],[3,4]]),
    ([1,3,6,10,15], [[1,3]]),
    ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.minimumAbsDifference(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
