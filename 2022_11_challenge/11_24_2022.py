# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter
from itertools import chain


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """LeetCode 79

        The precheck is crucial now, because the test case has included a case
        where if precheck is not included, it will TLE.

        This is the fourth time I have solved this problem.

        O(MNMN), 3488 ms, faster than 79.26%
        """
        M, N = len(board), len(board[0])
        # precheck
        bc = Counter(chain(*board))
        wc = Counter(word)
        for le, c in wc.items():
            if bc[le] < c:
                return False
        
        def search(i: int, j: int, idx: int) -> bool:
            if idx == len(word) - 1 and board[i][j] == word[idx]:
                return True
            if board[i][j] != word[idx]:
                return False
            board[i][j] = '.'  # visited
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < M and 0 <= nj < N and board[ni][nj] != '.':
                    if search(ni, nj, idx + 1):
                        return True
            board[i][j] = word[idx]
            return False

        for i in range(M):
            for j in range(N):
                if search(i, j, 0):
                    return True
        return False



sol = Solution()
tests = [
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED", True),
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE", True),
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB", False),
    ([["a"]], "a", True),
    ([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]], "AAAAAAAAAAAAAAB", False),
]

for i, (board, word, ans) in enumerate(tests):
    res = sol.exist(board, word)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
