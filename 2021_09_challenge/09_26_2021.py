# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter
import math


class Solution:
    def build_pat(self, lst: List[int]) -> int:
        """Build a pattern out of a given list of 1s and 0s"""
        n = len(lst)
        pat = 0
        for i in range(n):
            pat |= (lst[i] << (n - i - 1))
        return pat

    def count_swap(self, pat: int, val1: int, val2: int) -> int:
        """Count the min number of swaps to go from pat to either val1 or val2.

        Note that the number of 1s in the result of XOR must be even for swap
        to be possible

        :param pat: The current pattern.
        :param val1: One of the valid final pattern on the chessboard.
        :param val2: The other valid final pattern on the chessboard.
        """
        swap1 = bin(pat ^ val1).count('1')
        swap2 = bin(pat ^ val2).count('1')
        return min(
            swap1 if swap1 % 2 == 0 else math.inf,
            swap2 if swap2 % 2 == 0 else math.inf,
        ) // 2

    def movesToChessboard(self, board: List[List[int]]) -> int:
        """LeetCode 782

        This problem is not difficult in terms of using some smart algorithm.
        But it is complex because there are a lot of tricks to go through to
        help one realize that this problem does not require smart algorithm.

        First, we identify that to make a chessboard possible, each row must
        have equal number of 1s and 0s or the number of one value only one larger.
        If this requirement is not satisfied, we can return -1 immediately.

        Second, among all the rows, there must only be two patterns. This is
        because in the final chessboard, there are only two patterns for all the
        rows. Since swapping columns do not add or minus row patterns, we must
        start with two row patterns.

        Third, the two row patterns must complement each other. Otherwise, there
        must exist some swap on one row that will have no effect on the other
        row. e.g. pat1 = 0110, pat2 = 0010. Swapping the first two element of
        pat1 will not change pat2, which means we cannot make both patterns
        correct at the same time. This requirement can translate to pat1 ^ pat2
        = (1 << n) - 1)

        Fourth, the number of each row pattern must be equal or differ only by
        one.

        Interestingly, one the rows satisfy the above-mentioned four requirements
        the cols automatically also become valid. Then, we just need to find
        the min number of moves to swap the rows and the cols. Add them together,
        and we have the result. To find the min number of swaps, we create masks
        for the two valid final state val1, val2. We only need to check for one
        of the row and col pattern. We use XOR and then count the number of 1s
        in the result. The number of 1s indicate the number of mismatches
        between the current pattern and the valid pattern. Also, the number of
        1s must be even, because each pair of 1s indicate a swap. Odd number of
        1s doesn't work.

        O(N^2) time complexity. 76 ms, 88% ranking.
        """
        n = len(board)
        counter = Counter()
        mask = (1 << n) - 1
        for row in board:
            one_count = row.count(1)
            if abs(one_count - (n - one_count)) > 1:
                return -1
            counter[self.build_pat(row)] += 1
        if len(counter) != 2:
            return -1
        pat1, pat2 = counter.keys()
        if pat1 ^ pat2 != mask:
            return -1
        if abs(counter[pat1] - counter[pat2]) > 1:
            return -1
        # At this point, we are certain that the chessboard can be created.
        
        # Obtain the two valid states for each row and col
        val1 = 0
        for i in range(n - 1, -1, -2):
            val1 |= (1 << i)
        val2 = val1 ^ mask
        return self.count_swap(pat1, val1, val2) + self.count_swap(
            self.build_pat([board[i][0] for i in range(n)]),
            val1,
            val2,
        )


sol = Solution()
tests = [
    ([[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]], 2),
    ([[0, 1], [1, 0]], 0),
    ([[1, 0], [1, 0]], -1),
    ([[1, 1], [1, 0]], -1),
    ([[1, 1, 0], [0, 0, 1], [0, 0, 1]], 2),
]

for i, (board, ans) in enumerate(tests):
    res = sol.movesToChessboard(board)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
