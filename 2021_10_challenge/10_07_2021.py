# from pudb import set_trace; set_trace()
from typing import List
from itertools import chain
from collections import Counter


class Solution1:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """LeetCode 79

        The method is to first identify the position of the letter in board
        that matches the beginning of word. Then from there, we simply run a
        DFS with backtracking to check whether we have a matching path to word.
        One thing to keep in mind that we should not cache, because the result
        of matching or not from any position in board is dependent on the
        previous path. If the previous paths are not the same, then we cannot
        use the memoized value of the current position.

        Time complexity analysis from DBabichev is O(M*N*3^K), where M, N are
        the number of rows and cols of board, and K is the length of word. It's
        3^K instead of 4^K because at each level of DFS, we can only access
        three directions.

        4344 ms, 91% ranking.
        """
        pot_start = []
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    pot_start.append((i, j))
        if not pot_start:
            return False

        def search(i: int, j: int, idx: int) -> bool:
            if idx == len(word):
                return True
            cur = board[i][j]
            board[i][j] = '#'
            for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == word[idx]:
                    if search(ni, nj, idx + 1):
                        board[i][j] = cur
                        return True
            board[i][j] = cur
            return False

        return any(search(i, j, 1) for i, j in pot_start)


class Solution2:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """I have done this problem in July, 2020. Then, I submitted a solution
        with a smarter pre-check that I think resulted in significant
        improvement in time. This solution is exactly the same as Solution1,
        except that we will add the pre-check.

        With the pre-check, we reduce the run time to 1020 ms, 97% ranking.
        """
        board_count = Counter(chain(*board))
        word_count = Counter(word)
        for le, c in word_count.items():
            if board_count[le] < c:
                return False

        def search(i: int, j: int, idx: int) -> bool:
            if idx == len(word):
                return True
            cur = board[i][j]
            board[i][j] = '#'
            for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == word[idx]:
                    if search(ni, nj, idx + 1):
                        board[i][j] = cur
                        return True
            board[i][j] = cur
            return False

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if search(i, j, 1):
                        return True
        return False


sol = Solution2()
tests = [
    ([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCCED', True),
    ([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'SEE', True),
    ([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCB', False),
    ([['A', 'B', 'C', 'E'], ['S', 'F', 'E', 'S'], ['A', 'D', 'E', 'E']], 'ABCESEEEFS', True)
]

for i, (board, word, ans) in enumerate(tests):
    res = sol.exist(board, word)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
