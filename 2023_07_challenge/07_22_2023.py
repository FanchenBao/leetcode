# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter
from functools import lru_cache


class Solution1:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        """LeetCode 688

        BFS, using a counter as "queue" to count the number of times a cell has
        been visited in the current step.

        O(N^2 * K), 253 ms, faster than 67.80% 
        """
        queue = Counter([(row, column)])
        total = math.pow(8, k)
        while queue and k:
            tmp = Counter()
            for (i, j), c in queue.items():
                for di, dj in [(1, 2), (2, 1), (1, -2), (-2, 1), (-1, 2), (2, -1), (-1, -2), (-2, -1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        tmp[(ni, nj)] += c
            queue = tmp
            k -= 1
        return sum(queue.values()) / total


class Solution2:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        """Inspired by https://leetcode.com/problems/knight-probability-in-chessboard/solution/1980639

        The probability of a knight staying on the board at position i, j and
        having kth move is the mean probability of the knight staying on the
        board at all the eight next positions. This is a clear DP relationship,
        where dp(i, j, k) is the probability to find.

        O(N^2 * K), 226 ms, faster than 74.82%
        """
        moves = [(1, 2), (2, 1), (1, -2), (-2, 1), (-1, 2), (2, -1), (-1, -2), (-2, -1)]

        @lru_cache(maxsize=None)
        def dp(i: int, j: int, k: int) -> float:
            if not 0 <= i < n or not 0 <= j < n:
                return 0
            if k == 0:  # no more move and we are staying on the board
                return 1
            return sum(dp(i + di, j + dj, k - 1) for di, dj in moves) / 8

        return dp(row, column, k)


class Solution3:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        """The same as solution2, using DP, but we can save computation by
        taking advantage of symmetry. If two cells are symmetric around the
        center, across the mid line, or across the diagonal line, their
        probability are the same.

        This allows us to compute only the top right triangle of the top left
        corner of the board.

        Time complexity is the still the same O(N^2 * K), but the run time must
        be faster because we don't have to do a lot of repeated computation.

        113 ms, faster than 99.76%
        """
        moves = [(1, 2), (2, 1), (1, -2), (-2, 1), (-1, 2), (2, -1), (-1, -2), (-2, -1)]
        mid = n // 2

        @lru_cache(maxsize=None)
        def dp(i: int, j: int, k: int) -> float:
            if not 0 <= i < n or not 0 <= j < n:
                return 0
            if k == 0:  # no more move and we are staying on the board
                return 1
            if i > j or i > mid or j > mid:
                if i > j:  # diagonal symmetry
                    i, j = j, i
                i, j = min(i, n - 1 - i), min(j, n - 1 - j)  # mid line symmetry
                return dp(i, j, k)
            return sum(dp(i + di, j + dj, k - 1) for di, dj in moves) / 8

        return dp(row, column, k)


sol = Solution3()
tests = [
    (3, 2, 0, 0, 0.0625),
    (1, 0, 0, 0, 1),
]

for i, (n, k, row, column, ans) in enumerate(tests):
    res = sol.knightProbability(n, k, row, column)
    if math.isclose(res, ans):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
