# from pudb import set_trace; set_trace()
from typing import List
import copy


class Solution1:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """LeetCode 51

        Straightforward backtracking. Since the size of the board is quite
        small, we can make a deep copy of the board for the next round instead
        of actually "backtracking".

        O(?) 488 ms, 7% ranking.
        """
        res = []

        def helper(board: List[List[str]], row: int) -> None:
            if row == n:
                res.append([''.join(row) for row in board])
                return
            for col, p in enumerate(board[row]):
                if p == 'o':
                    board_cp = copy.deepcopy(board)
                    for j in range(n):
                        board_cp[row][j] = '.'
                    for i in range(n):
                        board_cp[i][col] = '.'
                    a, b = row, col
                    while a >= 0 and b >= 0:  # north west
                        board_cp[a][b] = '.'
                        a -= 1
                        b -= 1
                    a, b = row, col
                    while a >= 0 and b < 0:  # north east
                        board_cp[a][b] = '.'
                        a -= 1
                        b += 1
                    a, b = row, col
                    while a < n and b >= 0:  # south west
                        board_cp[a][b] = '.'
                        a += 1
                        b -= 1
                    a, b = row, col
                    while a < n and b < n:  # south east
                        board_cp[a][b] = '.'
                        a += 1
                        b += 1
                    board_cp[row][col] = 'Q'
                    helper(board_cp, row + 1)

        helper([['o'] * n for _ in range(n)], 0)
        return res


class Solution2:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """This is the solution from the official solution. The use of row - col
        and row + col to represent all diagonals that a queen can reach is the
        key trick in simplying this problem. Because we can use numerical values
        to represent the impossible positions, we don't even have to set up
        a chess board in the first place.

        O(N!) 56 ms, 84% ranking.
        """
        res = []
        cols = set()
        diag = set()  # upper left to lower right
        anti_diag = set()  # upper right to lower left

        def helper(row: int, queens: List[int]) -> None:
            if row == n:
                temp = []
                for q in queens:
                    r = ['.'] * n
                    r[q] = 'Q'
                    temp.append(''.join(r))
                res.append(temp)
                return
            for j in range(n):
                if j not in cols and row - j not in diag and row + j not in anti_diag:
                    queens.append(j)
                    cols.add(j)
                    diag.add(row - j)
                    anti_diag.add(row + j)
                    helper(row + 1, queens)
                    # backtracking
                    queens.pop()
                    cols.remove(j)
                    diag.remove(row - j)
                    anti_diag.remove(row + j)

        helper(0, [])
        return res


sol = Solution2()
tests = [
    (4, [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]),
    (1, [['Q']]),
]

for i, (n, ans) in enumerate(tests):
    res = sol.solveNQueens(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
