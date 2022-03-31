# from pudb import set_trace; set_trace()
from typing import List
from bisect import bisect_right


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """LeetCode 74

        Binary search the first column to obtain the row where target might be
        in. Then binary search that row.

        O(M + logM + logN), 59 ms, 59% ranking.
        """
        ci = bisect_right([row[0] for row in matrix], target)
        ri = bisect_right(matrix[ci - 1], target)
        return matrix[ci - 1][ri - 1] == target
        

sol = Solution()
tests = [
    ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3, True),
    ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13, False),
]

for i, (matrix, target, ans) in enumerate(tests):
    res = sol.searchMatrix(matrix, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
