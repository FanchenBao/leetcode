# from pudb import set_trace; set_trace()
from typing import List, Set
from functools import lru_cache


class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        """Didn't expect to solve this one, but fortunately, we did!

        It's a 3D DP. We need to ask ourselves in DP problem: what is the state
        of each DP call. In this case, i and j are naturally the state because
        they represent a unique position on the grid. In addition, we have the
        count of the left parenthesis as the state, because when we reach
        grid[i][j], we can come from different routes. And these routes can be
        represented by the number of left parentheses left. If at any time the
        number of left parentheses drops below zero, that path is invalid
        immediately. Otherwise, we carry out until hitting the last cell. And
        the check is simple: the last cell must be a right parenthesis and the
        cnt of left parentheses at that moment must be 1.

        And that's it. We use lru_cache to simplify the memoization process.
        O(MN(M+N)), 2626 ms, faster than 44.09%
        """
        M, N = len(grid), len(grid[0])
        
        @lru_cache(maxsize=None)
        def dfs(i: int, j: int, cnt: int) -> bool:
            if i >= M or j >= N or cnt < 0:
                return False
            if i == M - 1 and j == N - 1:
                return cnt == 1
            c = 1 if grid[i][j] == '(' else -1
            if dfs(i + 1, j, cnt + c) or dfs(i, j + 1, cnt + c):
                return True
            return False

        if grid[0][0] == ')' or grid[-1][-1] == '(':
            return False
        return dfs(0, 0, 0)


sol = Solution()
tests = [
    ([["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]], True),
    ([[")",")"],["(","("]], False),
    ([["(","(",")","(",")","(","(",")","(","(",")",")",")",")",")","(",")","(","(",")","(","(",")",")",")",")",")","(","(","(","("],[")","(","(","(",")","(",")","(","(",")",")",")",")","(",")",")","(","(",")",")","(",")","(",")","(","(",")","(",")","(","("],[")",")","(","(",")","(","(",")",")",")",")","(","(",")",")","(",")","(",")",")","(","(","(",")",")",")","(",")",")","(",")"],["(","(",")","(",")","(","(",")","(","(","(",")",")","(",")","(",")",")",")",")",")",")","(","(",")","(",")","(",")","(","("],[")",")","(",")",")","(","(","(",")",")","(",")","(",")",")",")","(","(","(",")",")","(",")","(",")",")","(","(","(","(",")"],[")",")","(","(",")","(",")","(",")","(",")","(",")",")","(",")","(",")",")","(",")","(","(","(",")","(",")",")",")","(","("],[")","(","(","(","(","(","(",")",")","(","(",")","(",")",")","(",")",")",")","(","(","(",")","(","(",")",")","(",")","(",")"],[")",")","(","(","(","(","(","(","(",")",")","(","(","(","(","(","(","(","(","(","(","(","(",")",")","(","(",")",")","(",")"],["(",")",")",")","(","(",")",")",")",")","(",")",")","(",")",")","(","(","(","(","(","(","(",")",")","(","(",")",")","(","("],["(","(",")","(",")",")",")",")","(","(","(",")",")",")","(",")","(","(",")","(","(","(",")","(","(","(","(","(",")",")",")"],["(",")","(","(","(","(",")","(","(",")",")","(","(",")","(","(","(",")","(","(","(",")",")","(",")",")","(",")","(","(",")"],[")",")","(","(","(","(",")","(","(",")",")","(",")",")","(",")","(","(","(","(","(","(","(",")","(","(",")",")","(","(","("],["(",")",")",")","(",")","(","(","(",")",")",")","(",")","(",")",")","(","(","(","(",")","(",")",")",")",")",")",")","(","("],["(","(","(","(","(","(",")",")","(",")","(","(","(",")",")","(",")","(",")","(",")","(","(","(",")",")",")","(",")","(","("],["(",")",")",")",")","(","(",")",")",")",")",")",")","(","(",")","(",")",")","(",")","(",")",")",")","(","(",")","(","(","("],["(",")",")","(","(",")",")","(",")",")","(","(","(",")",")",")",")","(","(","(",")",")","(",")","(","(","(","(",")",")",")"],[")","(","(",")","(","(",")",")",")","(","(","(","(",")","(",")",")",")","(",")","(",")","(","(",")","(","(","(","(","(","("],["(",")","(",")","(","(",")",")",")",")",")","(","(",")",")","(",")","(",")",")",")",")","(","(","(",")","(",")","(",")",")"],["(",")","(",")",")",")","(","(","(",")","(",")","(","(",")",")","(",")","(",")","(",")","(","(","(","(","(",")","(",")","("],[")",")",")",")",")","(",")",")","(","(",")","(",")",")","(",")",")","(","(","(","(",")","(","(","(","(",")",")",")",")","("],[")","(","(","(","(","(",")","(",")",")",")",")","(","(","(",")",")","(",")",")","(","(","(","(","(","(",")",")","(","(","("],["(","(","(",")",")","(",")","(",")",")",")",")","(",")",")",")",")","(",")","(","(","(","(",")","(","(","(","(","(","(",")"]], False),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.hasValidPath(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
