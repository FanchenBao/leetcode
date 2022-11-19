# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache
import sys

sys.setrecursionlimit(3000)


class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
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
            # print(turns)
            if turns >= 1000:
                return False
            if ci == mi and cj == mj:
                return False
            if ci == fi and cj == fj:
                return False
            if mi == fi and mj == fj:
                return True
            if is_mouse_turn:
                if helper(ci, cj, mi, mj, False, turns + 1):  # mouse stay
                    return True
                for d in range(1, mouseJump + 1):
                    for di, dj in [(d, 0), (-d, 0), (0, d), (0, -d)]:
                        nmi, nmj = mi + di, mj + dj
                        if 0 <= nmi < M and 0 <= nmj < N and grid[nmi][nmj] != '#':
                            if helper(ci, cj, nmi, nmj, False, turns + 1):
                                return True
                return False
            # cat's turn
            if not helper(ci, cj, mi, mj, True, turns + 1):  # cat stay
                return False
            for d in range(1, catJump + 1):
                for di, dj in [
                    (min(d, mi - ci) if mj == cj and mi > ci else d, 0),
                    (max(-d, mi - ci) if mj == cj and mi < ci else -d, 0),
                    (0, min(d, mj - cj) if mi == ci and mj > cj else d),
                    (0, max(-d, mj - cj) if mi == ci and mj < cj else -d),
                ]:
                    nci, ncj = ci + di, cj + dj
                    if 0 <= nci < M and 0 <= ncj < N and grid[nci][ncj] != '#':
                        if not helper(nci, ncj, mi, mj, True, turns + 1):
                            return False
            return True
            # print(ci, cj, mi, mj, is_mouse_turn, turns, f'{res=}')

        return helper(ini_ci, ini_cj, ini_mi, ini_mj, True, 0)


sol = Solution()
tests = [
    # (["####F","#C...","M...."], 1, 2, True),
    # (["M.C...F"], 1, 4, True),
    # (["M.C...F"], 1, 3, False),
    (["C...#","...#F","....#","M...."], 2, 5, False),
]

for i, (grid, catJumpm, mouseJump, ans) in enumerate(tests):
    res = sol.canMouseWin(grid, catJumpm, mouseJump)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
