# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """LeetCode 36

        Straightforward solution.

        O(N^2) 217 ms, faster than 51.04%
        """
        # check rows
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        # check cols
        for j in range(9):
            seen = set()
            for i in range(9):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        # check 3x3
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()
                for ii in range(i, i + 3):
                    for jj in range(j, j + 3):
                        if board[ii][jj] != '.':
                            if board[ii][jj] in seen:
                                return False
                            seen.add(board[ii][jj])
        return True


class Solution2:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """Bit masking.

        This is from the solution in 2021-08-20. The idea is to use bit masking
        to represent the state of each row, col, and 3x3. Then for each newly
        encountered value, we check the previous mask on row, col, and 3x3. If
        the current value has been encountered before, we turn false.

        O(N^2), 264 ms, faster than 16.47%
        """
        row, col, tbt = [0] * 9, [0] * 9, [0] * 9
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                mask = 1 << int(board[i][j])
                # check row and then update row
                if row[i] & mask:
                    return False
                row[i] |= mask
                # check col and then update col
                if col[i] & mask:
                    return False
                col[i] |= mask
                # check tbt (i.e. 3x3) and then update tbt
                idx = (i // 3) * 3 + j // 3
                if tbt[idx] & mask:
                    return False
                tbt[idx] |= mask
        return True



# sol = Solution()
# tests = [
#     ()
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
