# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """LeetCode 63

        The intuition is that the number of unique paths starting from any
        cell equals the sum of the unique paths starting from the cell to the
        right and the cell beheath. Using this relationship, we can solve the
        problem in a bottom up fashion. We first determine the number of unique
        paths starting from the cells on the right most col and bottom row,
        since there is only one way to go from there. And then we can expand
        backwards toward the starting point.

        The tricky part is when an obstacle happens on the right most col or
        bottom row, not only is that cell's unique paths equal to 0, but all
        the other cells above it or to the left of it are also assigned 0.

        O(MN) where M is the number of rows and N cols. 44 ms, 49% ranking.
        """
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * N for _ in range(M)]
        # Populate the right most col and bottom row
        val = 1
        for j in range(N - 1, -1, -1):
            if obstacleGrid[M - 1][j] == 1:
                val = 0
            dp[M - 1][j] = val
        val = 1
        for i in range(M - 1, -1, -1):
            if obstacleGrid[i][N - 1] == 1:
                val = 0
            dp[i][N - 1] = val
        # Populate the remaining cells
        for i in range(M - 2, -1, -1):
            for j in range(N - 2, -1, -1):
                dp[i][j] = 0 if obstacleGrid[i][j] else dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]


class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """1D array for dp. Same method as Solution1, but shrink the memroy use.

        Credit: https://leetcode.com/problems/unique-paths-ii/discuss/23250/Short-JAVA-solution
        """
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * N
        dp[N - 1] = int(obstacleGrid[M - 1][N - 1] == 0)
        for j in range(N - 2, -1, -1):  # prepare bottom row
            dp[j] = int(obstacleGrid[M - 1][j] == 0 and dp[j + 1] == 1)
        for i in range(M - 2, -1, -1):  # go through the rest of the grid
            for j in range(N - 1, -1, -1):
                if j == N - 1:
                    dp[j] = int(obstacleGrid[i][j] == 0 and dp[j] == 1)
                else:
                    dp[j] = 0 if obstacleGrid[i][j] else dp[j] + dp[j + 1]
        return dp[0]


class Solution3:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """This is almost a carbon copy of the solution in.

        Credit: https://leetcode.com/problems/unique-paths-ii/discuss/23250/Short-JAVA-solution

        except that we start from the bottom right corner going backwards to the
        upper left. A very brilliant solution.
        """
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * N
        dp[N - 1] = 1  # initialize
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if obstacleGrid[i][j]:
                    dp[j] = 0
                # note that we consider the right most column by not making any
                # update. This means, if we have a 1 in the cell below, we will
                # always have a 1 in the current cell as well. Otherwise, we
                # will always have a zero. Very smart.
                elif j != N - 1:
                    dp[j] += dp[j + 1]
        return dp[0]


sol = Solution3()
tests = [
    ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2),
    ([[0, 1], [0, 0]], 1),
    ([[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 30),
    ([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 70),
    ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 0),
    ([[0, 0], [0, 1]], 0),
    ([[0, 0]], 1),
]

for i, (obstacleGrid, ans) in enumerate(tests):
    res = sol.uniquePathsWithObstacles(obstacleGrid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
