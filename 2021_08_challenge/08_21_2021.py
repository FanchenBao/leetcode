# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        LeetCode 37

        Do not return anything, modify board in-place instead.

        I have struggled with this before, so I kinda remembered how this
        problem shall be approached. But the most help came from yesterday's
        problem which illuminates the superiority of using bitmap to check
        whether a value is feasible for a cell. Using bitmap significantly
        simplifies the procedure of validating a value and backtracking from a
        value. The rest is a simple DFS with backtracking, no special tricks.

        I always struggle to find the time complexity of a backtracking problem.
        So I don't know.

        132 ms, 80% ranking.

        UPDATE:

        hiepit claims that the time complexity is O(9^M) where M is the size of
        unknowns. It makes sense. Here is his post:

        https://leetcode.com/problems/sudoku-solver/discuss/1417032/C%2B%2BJavaPython-Backtracking-with-Bitmasking-Efficient-and-Clean

        DBabichev claims that the time complexity is O(1), which also makes
        sense because we know the upper bound of M. Here is his post:

        https://leetcode.com/problems/sudoku-solver/discuss/1416914/Python-backtracking-solution-explained
        """
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        # Obtain the initial state of the board
        unknowns = []  # a list of row and col indices
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    unknowns.append((i, j))
                else:
                    mask = 1 << int(board[i][j])
                    rows[i] |= mask
                    cols[j] |= mask
                    boxes[i // 3 * 3 + j // 3] |= mask
        
        def solver(idx: int) -> bool:
            if idx == len(unknowns):
                return True
            i, j = unknowns[idx]
            for k in range(1, 10):
                mask = 1 << k
                if not rows[i] & mask and not cols[j] & mask and not boxes[i // 3 * 3 + j // 3] & mask:
                    rows[i] |= mask
                    cols[j] |= mask
                    boxes[i // 3 * 3 + j // 3] |= mask
                    board[i][j] = str(k)
                    if solver(idx + 1):
                        return True
                    # backtracking
                    rows[i] ^= mask
                    cols[j] ^= mask
                    boxes[i // 3 * 3 + j // 3] ^= mask
                    board[i][j] = '.'
            return False

        solver(0)



# sol = Solution3()
# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
