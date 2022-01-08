# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """LeetCode 1463

        I wasn't able to figure this one out by myself, so I took a look at the
        hint. It suggested that I used DP to compute all possible states for
        the two robots. Basically, we have a 3D matrix, where for each row of
        the grid, we produce all possible combinations of indices of the two
        robots and compute the max number of cherries achievable for each
        combination. This way, we can build the algo bottom up, with each layer
        dependent on the layer below it. We produce all possible next step
        robot1 and robot2's index combinations, and pick the one that produces
        the max cherry picks. Once the matrix is built to the top, we simply
        return dp[0][0][-1].

        O(MN^2)
        """
        M, N = len(grid), len(grid[0])
        dp = [[[0] * N for _ in range(N)] for _ in range(M)]
        K = min(M, N)
        for j in range(K):  # col for robot 1
            for k in range(N - K, N):  # col for robot 2
                if j != k:
                    dp[-1][j][k] = grid[-1][j] + grid[-1][k]
                else:
                    dp[-1][j][k] = grid[-1][j]
        for i in range(M - 2, -1, -1):
            max_hor_cnt = min(i + 1, N)
            for j in range(max_hor_cnt):
                for k in range(N - max_hor_cnt, N):
                    # produce all possible combination for the next round
                    max_next = 0
                    for r1 in range(j - 1, j + 2):
                        for r2 in range(k - 1, k + 2):
                            if 0<= r1 < N and 0 <= r2 < N:
                                max_next = max(max_next, dp[i + 1][r1][r2])
                    if j != k:
                        dp[i][j][k] = max_next + grid[i][j] + grid[i][k]
                    else:
                        dp[i][j][k] = max_next + grid[i][j]
        return dp[0][0][-1]



sol = Solution()
tests = [
    ([[3,1,1],[2,5,1],[1,5,5],[2,1,1]], 24),
    ([[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]], 28),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.cherryPickup(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
