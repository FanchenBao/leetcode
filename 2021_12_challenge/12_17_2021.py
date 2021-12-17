# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """LeetCode 221

        I have solved this less than a month ago, so the solution is still with
        me. However, it still took me two tries to pass the OJ. DP solution.
        At each new cell, we check the cell to the left, above, and diagonally
        to the upperleft to find the min side of square. Then the current cell's
        side of square is that min value plus one.

        O(N^2), 336 ms, 16% ranking.

        # UPDATE: by reducing conditional checks, we can speed up the runtime.
        212 ms, 59% ranking.
        """
        N = len(matrix[0])
        dp = [0] + [int(c) for c in matrix[0]]
        res = int(any(dp))
        for row in matrix[1:]:
            temp = [0]
            for j in range(1, N + 1):
                if row[j - 1] == '0':
                    temp.append(0)
                else:
                    temp.append(1 + min(dp[j], dp[j - 1], temp[j - 1]))
                    res = max(res, temp[-1])
            dp = temp
        return res**2


sol = Solution()
tests = [
    ([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]], 4),
    ([["0","1"],["1","0"]], 1),
    ([["0"]], 0),
    ([['1']], 1),
    ([["1","1"]], 1),
]

for i, (matrix, ans) in enumerate(tests):
    res = sol.maximalSquare(matrix)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
