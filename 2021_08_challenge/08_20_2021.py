# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """LeetCode 36

        The problem itself is not difficult. It's not like we are solving the
        sudoku. To validate, we simply check all rows, all columns, and all 3x3
        If there happens to be repeated values, we return False. Otherwise, if
        all checks pass, we return True.

        I have disagreement with the OJ. The OJ will pass a sudoku that contains
        0, but in the requirement it is specified that 0 is not allowed. Thus,
        I think the OJ is not correct.

        Since the board is restricted to 9x9, the time complexity is O(1).

        100 ms, 48% ranking.
        """
        # check rows
        for i in range(9):
            temp = set([0])
            for j in range(9):
                di = int(board[i][j])
                if di in temp:
                    return False
                temp.add(di)
        # check cols
        for j in range(9):
            temp = set([0])
            for i in range(9):
                di = int(board[i][j])
                if di in temp:
                    return False
                temp.add(di)
        # check 3x3
        for p in range(0, 9, 3):
            for q in range(0, 9, 3):
                temp = set([0])
                for k in range(9):
                    di = int(board[p + k // 3][q + k % 3])
                    if di in temp:
                        return False
                    temp.add(di)
        return True


class Solution2:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """Use bitmasking"""
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9  # see below how to get idx for each box from i and j
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                mask = 1 << int(board[i][j])
                # Check rows
                if rows[i] & mask:
                    return False
                rows[i] |= mask
                # Check cols
                if cols[j] & mask:
                    return False
                cols[j] |= mask
                # Check boxes
                bi = (i // 3) * 3 + j // 3  # convert i and j into box index
                if boxes[bi] & mask:
                    return False
                boxes[bi] |= mask
        return True


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
