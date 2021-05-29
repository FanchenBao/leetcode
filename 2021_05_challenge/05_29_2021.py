# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        """LeetCode 52

        This is an easier version of the origina N-queens, because we are
        not required to output the actual solution, which means we don't have
        to track the positions of each queen. That said, the idea is exactly
        the same as the previous N-queen problem. We just increment a counter
        once a solution is found. Since each solution always corresponds to
        at least one unique queen position, all solutions are unique. In other
        words, when we find a solution, there is no need to check for uniqueness

        Also the same trick of using sum and difference of the row and col
        indices to represent diagonals is applicable as well.

        O(N!) 52 ms, 65% ranking.
        """
        cols = set()
        d1 = set()  # northwest to southeast
        d2 = set()  # northest to southwest
        res = [0]

        def backtrack(row: int) -> None:
            if row == n:
                res[0] += 1
            else:
                for col in range(n):
                    if col in cols or (row + col) in d2 or (row - col) in d1:
                        continue
                    cols.add(col)
                    d1.add(row - col)
                    d2.add(row + col)
                    backtrack(row + 1)
                    cols.remove(col)
                    d1.remove(row - col)
                    d2.remove(row + col)

        backtrack(0)
        return res[0]


sol = Solution()
tests = [
    (4, 2),
    (1, 1),
]

for i, (n, ans) in enumerate(tests):
    res = sol.totalNQueens(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
