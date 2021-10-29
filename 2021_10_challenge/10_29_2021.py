# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """The main problem is how do we tell that an orange is rotten from the
        previous round or from the current round. If we are at a fresh orange,
        and its neighbor has just rotten in the current round, then we should
        not rot the orange. Otherwise, if the neighbor has rotten in a previous
        round, then we shall rot as well.

        To resolve this issue, we use a temp value to indicate at which "round"
        an orange has rotten. Thus, if a frensh orange sees that its neighbor
        is rotten in the same "round" as right now, it does not rot. Otherwise,
        it does. The reason that I put quotes on round is that the temp value
        is not strictly the round. It starts from 3 and going upwards. We cannot
        start from 0, because 0 and 1 have different meanings. At the end, we
        can compute the number of rounds by doing temp - res.

        Also, we need to keep track of the number of fresh oranges and whether
        any additional orange has rotten. If there is no more new rotten orange,
        that means we have terminated.

        It is also worth checking my solution from more than a year go, where
        we uses a queue and a global count of fresh oranges to keep track of the
        current state of the grid.

        O(MNR), where M, N are the dimensions of the grid and R is the total
        number of rounds. 52 ms, 79% ranking.
        """
        res, temp = 3, 3
        M, N = len(grid), len(grid[0])
        while True:
            rotten = False
            num_fresh = 0
            for i in range(M):
                for j in range(N):
                    if grid[i][j] == 1:
                        num_fresh += 1
                        for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                            if 0 <= ni < M and 0 <= nj < N:
                                if 2 <= grid[ni][nj] < temp:  # rotten in previous rounds
                                    grid[i][j] = temp
                                    rotten = True
            if not rotten:
                break
            temp += 1
        return (temp - res) if not num_fresh else -1


sol = Solution()
tests = [
    ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
    ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),
    ([[0, 2]], 0),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.orangesRotting(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
