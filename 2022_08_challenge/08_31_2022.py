# from pudb import set_trace; set_trace()
from typing import List, Set, Tuple


class Solution1:

    def update(self, heights, dp) -> bool:
        M, N = len(heights), len(heights[0])
        has_change = False
        for i in range(M):
            for j in range(N):
                for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < M and 0 <= nj < N and heights[i][j] >= heights[ni][nj] and dp[i][j] != 3:
                        tmp = dp[i][j]
                        dp[i][j] |= dp[ni][nj]
                        if tmp != dp[i][j]:
                            has_change = True
        return has_change

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """LeetCode 417

        This is very bad. Basically traverse the heights as many time as
        possible until it stabilizes. Terrible idea, but works.

        1857 ms, 8%
        """
        M, N = len(heights), len(heights[0])
        dp = [[0] * N for _ in range(M)]
        # first round, check for Pacific
        for i in range(M):
            for j in range(N):
                dp[i][j] |= (i == 0 or ((heights[i][j] >= heights[i - 1][j]) and dp[i - 1][j])) | (j == 0 or ((heights[i][j] >= heights[i][j - 1]) and dp[i][j - 1]))
        # second round, check for Atlantic
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                dp[i][j] |= (((i == M - 1) and 2) or ((heights[i][j] >= heights[i + 1][j]) and dp[i + 1][j])) | (((j == N - 1) and 2) or ((heights[i][j] >= heights[i][j + 1]) and dp[i][j + 1]))
        # update until stabilized
        while self.update(heights, dp):
            pass
        return [[i, j] for i in range(M) for j in range(N) if dp[i][j] == 3]


class Solution2:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """This is the correct solution.

        We use DFS to find all the cells that can reach pacific, and all the
        cells that can reach atlantic. Then find their intersection. Done.

        This works, because we have deterministic starts. We know the first
        row and first column must reach pacific. They serve as the starting
        point for DFS to find all the cells that can reach the Pacific. The
        same goes for the Atlantic.

        804 ms, faster than 11.75%
        """
        M, N = len(heights), len(heights[0])
        p_reachable, a_reachable = set(), set()

        def dfs(i: int, j: int, reachable: Set[Tuple[int, int]]) -> None:
            reachable.add((i, j))
            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                ni, nj = i + di, j + dj
                if 0 <= ni < M and 0 <= nj < N and (ni, nj) not in reachable and heights[ni][nj] >= heights[i][j]:
                    dfs(ni, nj, reachable)

        for i in range(M):
            dfs(i, 0, p_reachable)
            dfs(i, N - 1, a_reachable)
        for j in range(N):
            dfs(0, j, p_reachable)
            dfs(M - 1, j, a_reachable)
        return list(p_reachable.intersection(a_reachable))


sol = Solution2()
tests = [
    ([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]], [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]),
    ([[1]], [[0,0]]),
    ([[1,2,3],[8,9,4],[7,6,5]], [[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]),
    ([[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]], [[0,3],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3],[3,0],[3,1],[3,2],[3,3]]),
    ([[8,13,11,18,14,16,16,4,4,8,10,11,1,19,7],[2,9,15,16,14,5,8,15,9,5,14,6,10,15,5],[15,16,17,10,3,6,3,4,2,17,0,12,4,1,3],[13,6,13,15,15,16,4,10,7,4,19,19,4,9,13],[7,1,9,14,9,11,5,4,15,19,6,0,0,13,5],[9,9,15,12,15,5,1,1,18,1,2,16,15,18,9],[13,0,4,18,12,0,11,0,1,15,1,15,4,2,0],[11,13,12,16,9,18,6,8,18,1,5,12,17,13,5],[7,17,2,5,0,17,9,18,4,13,6,13,7,2,1],[2,3,9,0,19,6,6,15,14,4,8,1,19,5,9],[3,10,5,11,7,14,1,5,3,19,12,5,2,13,16],[0,8,10,18,17,5,5,8,2,11,5,16,4,9,14],[15,9,16,18,9,5,2,5,13,3,10,19,9,14,3],[12,11,16,1,10,12,6,18,6,6,18,10,9,5,2],[17,9,6,6,14,9,2,2,13,13,15,17,15,3,14],[18,14,12,6,18,16,4,10,19,5,6,8,9,1,6]], [[0,13],[0,14],[1,13],[11,3],[12,0],[12,2],[12,3],[13,0],[13,1],[13,2],[14,0],[15,0]]),
    ([[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]], [[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0],[2,1],[2,2],[2,3],[2,4],[3,0],[3,1],[3,2],[3,3],[3,4],[4,0],[4,1],[4,2],[4,3],[4,4]]),
    ([[7,1,17,13,9,10,5,14,0,3],[7,15,7,8,15,16,10,10,5,13],[18,9,15,8,19,16,7,5,5,10],[15,11,18,3,1,17,6,4,10,19],[3,16,19,12,12,19,2,14,5,9],[7,16,0,13,14,7,2,8,6,19],[5,10,1,10,2,12,19,1,0,19],[13,18,19,12,17,17,4,5,8,2],[2,1,17,13,14,12,14,2,16,10],[5,8,1,11,16,1,18,15,6,19],[3,8,14,14,5,0,2,7,5,1],[17,1,9,17,10,10,10,7,1,16],[14,18,5,11,17,15,8,8,14,13],[6,4,10,17,8,0,11,4,2,8],[16,11,17,9,3,2,11,0,6,5],[12,18,18,11,1,7,12,16,12,12],[2,14,12,0,2,8,5,10,7,0],[16,13,1,19,8,13,11,8,11,3],[11,2,8,19,6,14,14,6,16,12],[18,0,18,10,16,15,15,12,4,3],[8,15,9,13,8,2,6,11,17,6],[7,3,0,18,7,12,2,3,12,10],[7,9,13,0,11,16,9,9,12,13],[9,4,19,6,8,10,12,6,7,11],[5,9,18,0,4,9,6,4,0,1],[9,12,1,11,13,13,0,16,0,6],[7,15,4,8,15,17,17,19,15,1],[7,17,4,1,1,14,10,19,10,19],[10,5,12,5,8,8,14,14,6,0],[16,10,10,7,13,4,0,15,18,0],[11,2,10,6,5,13,4,5,3,1],[9,14,16,14,15,3,2,13,17,8],[19,2,10,1,2,15,12,10,2,5],[12,4,8,9,8,6,4,14,14,0],[11,17,17,4,16,13,6,15,5,7],[12,18,1,3,9,10,7,1,1,1],[18,6,10,8,12,14,9,12,10,3],[15,13,18,13,8,5,12,14,18,0],[15,4,8,9,19,18,6,19,12,0],[4,14,15,4,17,17,9,17,9,0],[6,17,16,10,3,8,8,18,15,9],[3,8,4,2,13,0,2,8,8,2],[14,12,13,12,17,4,16,9,8,7],[0,19,8,16,1,13,7,6,15,11],[1,13,16,14,10,4,11,19,9,13],[8,0,2,1,16,12,16,9,9,9],[5,2,10,4,8,12,17,0,2,15],[11,2,15,15,14,9,11,19,18,11],[4,4,1,5,13,19,9,17,17,17],[4,1,8,0,8,19,11,0,5,4],[8,16,14,18,12,2,0,19,0,13],[7,11,3,18,8,2,2,19,8,7],[3,13,6,1,12,16,4,13,0,5],[12,1,16,19,2,12,16,15,19,6],[1,7,12,15,3,3,13,17,16,12]], [[0,9],[1,9],[2,9],[3,9],[11,3],[53,0],[53,2],[53,3],[54,0],[54,1],[54,2],[54,3]]),
]

for i, (heights, ans) in enumerate(tests):
    res = [[i, j] for i, j in sol.pacificAtlantic(heights)]
    res.sort()
    ans.sort()
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
