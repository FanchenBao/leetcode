# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        LeetCode 130

        The insight is that any Os that are connected to an O on the edge cannot
        be turned. Thus, we can search around the edge to find the seeding O
        that cannot be turned. From there, we use dfs to mark all the Os that
        cannot be turned. We use '#' for this mark. Once we go through all four
        edges, we will have marked all non-turnable Os. Finally, we traverse the
        entire grid again and turn all the '#' to 'O', and all the 'O' (turnable
        Os) to 'X'.

        O(MN), where M is the height and N the width of the board.

        136 ms, 83% ranking.
        """
        M, N = len(board), len(board[0])
        
        def dfs(i: int, j: int) -> None:
            board[i][j] = '#'
            for ni, nj in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if 0 <= ni < M and 0 <= nj < N and board[ni][nj] == 'O':
                    dfs(ni, nj)

        for j in range(N):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[M - 1][j] == 'O':
                dfs(M - 1, j)
        for i in range(M):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][N - 1] == 'O':
                dfs(i, N - 1)
        for i in range(M):
            for j in range(N):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        

sol = Solution()
tests = [
    ([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]],[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]),
    ([["X"]],[["X"]]),
    ([["X","X","X","X"],["X","O","O","X"],["X","O","O","X"],["X","O","X","X"]],[["X","X","X","X"],["X","O","O","X"],["X","O","O","X"],["X","O","X","X"]]),
]

for i, (board, ans) in enumerate(tests):
    sol.solve(board)
    if board == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {board}')
