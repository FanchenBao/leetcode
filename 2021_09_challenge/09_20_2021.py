# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def tictactoe(self, moves: List[List[int]]) -> str:
        """LeetCode 1275

        This is an easy question. We only need to figure out a scheme to
        record the number of characters each player accumulates for all rows,
        cols, and diags. My choise is an array of size 8. I use the first three
        pos to record the accumulation on row 0, 1, 2. The next three for col
        0, 1, 2. And the last two for down right and down left diags. The only
        trick I see is that the down right diag is defined by coordinates where
        i == j, and the down left diag is defined by i + j == 2.

        Let's call the time complexity as O(1).

        65 ms, 5% ranking.
        """
        players = [[0] * 8, [0] * 8]
        for idx, (i, j) in enumerate(moves):
            pi = idx % 2
            players[pi][i] += 1
            players[pi][j + 3] += 1
            if i == j:
                players[pi][6] += 1
            if i + j == 2:
                players[pi][7] += 1
        if any(c == 3 for c in players[0]):
            return 'A'
        if any(c == 3 for c in players[1]):
            return 'B'
        if len(moves) == 9:
            return 'Draw'
        return 'Pending'


class Solution2:
    def tictactoe(self, moves: List[List[int]]) -> str:
        """This is from the official solution.

        https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/solution/

        It's very smart. Kind of similar idea as Solution1, but we only use one
        array to record for both A and B. Except when A makes a move, we add 1.
        When B moves, we deduct 1. At each move, we check whether the array
        contains any value whose absolute value is three. If no winner is
        available, check the moves to determine whether we it's pending or draw.
        """
        plays = [0] * 8
        pl = 1
        for i, j in moves:
            plays[i] += pl
            plays[j + 3] += pl
            if i == j:
                plays[6] += pl
            if i + j == 2:
                plays[7] += pl
            if any(abs(p) == 3 for p in plays):
                return 'A' if pl == 1 else 'B'
            pl *= -1
        return 'Draw' if len(moves) == 9 else 'Pending'


sol = Solution2()
tests = [
    ([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]], 'A'),
    ([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]], 'B'),
    ([[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]], 'Draw'),
    ([[0, 0], [1, 1]], 'Pending'),
]

for i, (moves, ans) in enumerate(tests):
    res = sol.tictactoe(moves)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
