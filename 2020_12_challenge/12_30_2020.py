# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """Use binary code to indicate the previous and current state:

        00: 0 -> 0, remain dead
        01: 0 -> 1, reproduce
        10: 1 -> 0, die
        11: 1 -> 1, remain alive

        To simplify the code, all the 1s in the initial board is replaced with
        3. At each cell, we count the number of previous alive cells in the
        neighbors, i.e. the number of 2s and 3s in the eight neigbors. Once a
        decision is made for the current state, we use one of the four numbers
        for representation.

        After the board is done, we revert the binary code to 1s and 0s, in
        particular all 2s and 0s are 0, and all 1s and 3s are 1.

        O(MxN), O(1) space, 36 ms, 43% ranking.
        """
        m = len(board)
        n = len(board[0])

        def count_live(i, j):
            count = 0
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if (di or dj) and 0 <= i + di < m and 0 <= j + dj < n:
                        count += 1 if board[i + di][j + dj] in {2, 3} else 0
            return count

        # prepare the board
        for i in range(m):
            for j in range(n):
                board[i][j] = 3 if board[i][j] else 0
        # update the board
        for i in range(m):
            for j in range(n):
                num_live = count_live(i, j)
                if board[i][j] and (num_live < 2 or num_live > 3):
                    board[i][j] = 2
                elif not board[i][j] and num_live == 3:
                    board[i][j] = 1
        # present the board
        for i in range(m):
            for j in range(n):
                board[i][j] = 1 if board[i][j] in {3, 1} else 0


class Solution2:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """Use a smarter coding system to avoid the initial set up of the board.

        -1 = 0 -> 1
        1 = original 1
        0 = original 0
        2 = 1 -> 0

        O(MN), O(1) space, 36 ms, 43% ranking.
        """
        m = len(board)
        n = len(board[0])

        def count_live(i, j):
            count = 0
            for I in range(i - 1, i + 2):
                for J in range(j - 1, j + 2):
                    if (I != i or J != j) and 0 <= I < m and 0 <= J < n:
                        count += 1 if board[I][J] in {1, 2} else 0
            return count

        # update the board
        for i in range(m):
            for j in range(n):
                num_live = count_live(i, j)
                if board[i][j] == 1 and (num_live < 2 or num_live > 3):
                    board[i][j] = 2
                elif not board[i][j] and num_live == 3:
                    board[i][j] = -1
                print(i, j, num_live, board)
        # present the board
        for i in range(m):
            for j in range(n):
                board[i][j] = 1 if board[i][j] in {1, -1} else 0


sol = Solution2()
tests = [
    ([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]], [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]),
    ([[1, 1], [1, 0]], [[1, 1], [1, 1]]),
]

for i, (board, ans) in enumerate(tests):
    res = sol.gameOfLife(board)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
