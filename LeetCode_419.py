# from pudb import set_trace; set_trace()
from typing import List



class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        """Since we scan the board left to right and top to bottom, we will
        always encounter the beginning of a ship. And the beginning is
        characterized by an 'X' with the cell to the top and left of 'X' NOT
        being 'X'. Thus, all we need to do is to count the number of the start
        of each ship, regardless of whether they are horizontal or vertical.

        O(MN), 124 ms, 8% ranking.
        """
        res = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    if (j == 0 or board[i][j - 1] == '.') and (i == 0 or board[i - 1][j] == '.'):
                        res += 1
        return res


sol = Solution()
tests = [
    ([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]], 2),
    ([["."]], 0)
]

for i, (board, ans) in enumerate(tests):
    res = sol.countBattleships(board)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
