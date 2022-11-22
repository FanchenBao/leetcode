# from pudb import set_trace; set_trace()
from typing import List, Tuple
import math
from functools import lru_cache


class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        """I almost solved this, but I kept getting TLE. I was missing two
        important insights.

        1. cat or mouse's turn can be determined by whether `turns` is even or
        odd. There is no need to use another variable.

        2. The max number of turns that can be taken is M * N * 2, i.e. when
        both cat and mouse only takes one step at a time, and they cover the
        search of the entire grid. Once that is reached, there is no way that
        either of them can win out right. This means, it is guaranteed that
        eventually we will hit 1000 turns and cat would win. However, we don't
        have to wait until 1000 turns. We can terminate when M * N * 2 turns
        have been reached.

        Both insights come from this post: https://leetcode.com/problems/cat-and-mouse-ii/discuss/1020616/Python3-Clean-and-Commented-Top-down-DP-with-the-early-stopping-trick

        7158 ms, faster than 30.00%

        UPDATE:

        1. use available cells not total number of cells as constraints.
        2. mouse cannot stay, but cat can

        5041 ms, faster than 60.00%
        """
        M, N = len(grid), len(grid[0])
        available = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 'C':
                    ini_ci, ini_cj = i, j
                if grid[i][j] == 'M':
                    ini_mi, ini_mj = i, j
                if grid[i][j] != '#':
                    available += 1

        @lru_cache(maxsize=None)
        def helper(ci: int, cj: int, mi: int, mj: int, turns: int) -> bool:
            if turns > available * 2:
                return False
            if ci == mi and cj == mj:  # cat reaches mouse
                return False
            if grid[ci][cj] == 'F':  # cat reaches food
                return False
            if grid[mi][mj] == 'F':  # mouse reaches food
                return True
            if turns % 2 == 0:
                # mouse cannot stay. Because if it does, cat can also stay
                # and eventually cat would win. Thus, mouse must move.
                # Courtesy: https://leetcode.com/problems/cat-and-mouse-ii/discuss/1020616/Python3-Clean-and-Commented-Top-down-DP-with-the-early-stopping-trick/841206
                for ui, uj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    for d in range(1, mouseJump + 1):
                        di, dj = ui * d, uj * d
                        nmi, nmj = mi + di, mj + dj
                        if 0 <= nmi < M and 0 <= nmj < N and grid[nmi][nmj] != '#':
                            if helper(ci, cj, nmi, nmj, turns + 1):
                                return True
                        else:  # either going outside or hit a wall
                            break
                return False

            # cat's turn
            if not helper(ci, cj, mi, mj, turns + 1):  # cat stay
                return False
            for ui, uj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                for d in range(1, catJump + 1):
                    di, dj = ui * d, uj * d
                    nci, ncj = ci + di, cj + dj
                    if nci == mi and ncj == mj:
                        return False
                    if 0 <= nci < M and 0 <= ncj < N and grid[nci][ncj] != '#':
                        if not helper(nci, ncj, mi, mj, turns + 1):
                            return False
                    else:  # either going outside or hit a wall
                        break
            return True

        return helper(ini_ci, ini_cj, ini_mi, ini_mj, 0)


sol = Solution()
tests = [
    (["####F","#C...","M...."], 1, 2, True),
    (["M.C...F"], 1, 4, True),
    (["M.C...F"], 1, 3, False),
    (["C...#","...#F","....#","M...."], 2, 5, False),
    ([".....","...C.","...#.","...#M","F..#."], 1, 3, True),
    (["####.##",".#C#F#.","######.","##M.###"], 3, 6, False),
]

for i, (grid, catJumpm, mouseJump, ans) in enumerate(tests):
    res = sol.canMouseWin(grid, catJumpm, mouseJump)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
