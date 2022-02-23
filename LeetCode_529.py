# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        """Not a difficult one but quite entertaining. The main trick is to
        understand when the recursive clicking ends. It ends whenever the
        current spot has been revealed, which means it has the value 'B', 'M',
        or integer 1 through 8. These are the anchor cases.

        Otherwise, we need to make sure whether the current spot, marked by
        'E', is a 'B' or a number. This means we need to check for the number
        of mines around the current spot. If the number is 0, we mark the
        current as 'B', otherwise the number of mines. Then we simply recurse.

        O(MN), 254 ms, 55% ranking.
        """
        M, N = len(board), len(board[0])
        
        def dfs(i, j):
            if board[i][j] == 'B' or '1' <= board[i][j] <= '8':
                return
            if board[i][j] == 'M':
                board[i][j] = 'X'
                return
            num_mines = sum(0 <= p < M and 0 <= q < N and board[p][q] == 'M' for p in range(i - 1, i + 2) for q in range(j - 1, j + 2))
            if num_mines > 0:
                board[i][j] = str(num_mines)
                return
            board[i][j] = 'B'
            for p in range(i - 1, i + 2):
                for q in range(j - 1, j + 2):
                    if 0 <= p < M and 0 <= q < N:
                        dfs(p, q)

        dfs(*click)
        return board



sol = Solution()
tests = [
    ([4,2,1,3], [[1,2],[2,3],[3,4]]),
    ([1,3,6,10,15], [[1,3]]),
    ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.minimumAbsDifference(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
