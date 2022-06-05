# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """LeetCode 51

        One of the most classic problems in DFS with backtracking. I have
        solved this three times before and still remember the most important
        trick: the top left to bottom right diagonals have the sum of the row
        and col indices the same, and the top right to bottom left diagonals
        have the diff of the row and col indices the same. Armed with these
        two tricks, the problem is not difficult to handle.

        O(N^2), 92 ms, faster than 55.94%
        """
        grid = [['.'] * n for _ in range(n)]
        res = []
        not_c = set()  # not available col
        not_tlbr = set()  # not available diagonal, top left to bottom right
        not_trbl = set()  # not available diagonal, top right to bottom left

        def dfs(r: int) -> None:
            if r == n:
                res.append([''.join(row) for row in grid])
                return
            for c in range(n):
                if c not in not_c and r - c not in not_tlbr and r + c not in not_trbl:
                    not_c.add(c)
                    not_tlbr.add(r - c)
                    not_trbl.add(r + c)
                    grid[r][c] = 'Q'
                    dfs(r + 1)
                    # backtrack
                    not_c.remove(c)
                    not_tlbr.remove(r - c)
                    not_trbl.remove(r + c)
                    grid[r][c] = '.'

        dfs(0)
        return res


sol = Solution()
tests = [
    (4, [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]),
]

for i, (n, ans) in enumerate(tests):
    res = sol.solveNQueens(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
