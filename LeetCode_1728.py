# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache
import sys

sys.setrecursionlimit(3000)


class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        """TLE.
        """
        M, N = len(grid), len(grid[0])
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 'C':
                    ini_ci, ini_cj = i, j
                if grid[i][j] == 'M':
                    ini_mi, ini_mj = i, j
                if grid[i][j] == 'F':
                    fi, fj = i, j

        @lru_cache(maxsize=None)
        def helper(ci: int, cj: int, mi: int, mj: int, is_mouse_turn: bool, turns: int) -> bool:
            if turns >= 1000:
                return False
            if ci == mi and cj == mj:  # cat reaches mouse
                return False
            if ci == fi and cj == fj:  # cat reaches food
                return False
            if mi == fi and mj == fj:  # mouse reaches food
                return True
            if is_mouse_turn:
                for ui, uj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    for d in range(1, mouseJump + 1):
                        di, dj = ui * d, uj * d
                        nmi, nmj = mi + di, mj + dj
                        if 0 <= nmi < M and 0 <= nmj < N and grid[nmi][nmj] != '#':
                            if helper(ci, cj, nmi, nmj, False, turns + 1):
                                return True
                        else:  # either going outside or hit a wall
                            break
                return False

            # cat's turn
            for ui, uj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                for d in range(1, catJump + 1):
                    di, dj = ui * d, uj * d
                    nci, ncj = ci + di, cj + dj
                    if nci == mi and ncj == mj:
                        return False
                    if 0 <= nci < M and 0 <= ncj < N and grid[nci][ncj] != '#':
                        if not helper(nci, ncj, mi, mj, True, turns + 1):
                            return False
                    else:  # either going outside or hit a wall
                        break
            return True
            # print(ci, cj, mi, mj, is_mouse_turn, turns, f'{res=}')

        return helper(ini_ci, ini_cj, ini_mi, ini_mj, True, 0)


sol = Solution()
tests = [
    (["####F","#C...","M...."], 1, 2, True),
    (["M.C...F"], 1, 4, True),
    (["M.C...F"], 1, 3, False),
    (["C...#","...#F","....#","M...."], 2, 5, False),
    ([".....","...C.","...#.","...#M","F..#."], 1, 3, True),
]

for i, (grid, catJumpm, mouseJump, ans) in enumerate(tests):
    res = sol.canMouseWin(grid, catJumpm, mouseJump)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
