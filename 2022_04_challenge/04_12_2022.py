# from pudb import set_trace; set_trace()
from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        LeetCode 289

        Use sentinel values to indicate whether a cell changes from 1 to 0 or
        0 to 1. In the implementation below, 1 -> 0 change is marked as -1, and
        0 -> 1 change is marked as 2. So when we examine for the number of
        living cells, we just need to check how many neighbors have abs value
        of 1.

        O(MN), 38 ms, 75.43%

        UPDATE: use smarter way to check for live cells.
        """
        M, N = len(board), len(board[0])
        for i in range(M):
            for j in range(N):
                num_alive = 0
                for ni in range(i - 1, i + 2):
                    for nj in range(j - 1, j + 2):
                        if 0 <= ni < M and 0 <= nj < N and (ni != i or nj != j):
                            num_alive += abs(board[ni][nj]) == 1
                if board[i][j] == 1 and (num_alive < 2 or num_alive > 3):
                    board[i][j] = -1
                elif board[i][j] == 0 and num_alive == 3:
                    board[i][j] = 2
        for i in range(M):
            for j in range(N):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1


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
