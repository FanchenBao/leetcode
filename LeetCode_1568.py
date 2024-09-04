# from pudb import set_trace; set_trace()
from typing import List, Optional, Tuple
import math


class Solution:
    TIME = 0

    def does_articulation_exist(
        self,
        i: int,
        j: int,
        grid: List[List[int]],
        disc: List[List[int]],
        low_disc: List[List[int]],
        par: List[List[Optional[Tuple[int, int]]]],
    ) -> bool:
        """
        Use Tarjan to detect whether an articulation node exist in the given
        grid.

        disc: discovery time during a DFS tree
        low_disc: the lowest discovery time of the ancestor to the subtree that
        contains the current node (i, j)
        par: the parent node of all the nodes

        Tarjan's algo stipulates that a node is an articulation iff one of the
        two conditions below is satisfied.

        1. the current node (i, j) is a root in the DFS tree and it has two
        children.
        2. the current node is NOT a root AND its discovery time is smaller
        or equal to the smallest discovery time of any ancestors to the current
        node's subtree (i.e., disc[i][j] <= low_disc[ni][nj])
        """
        M, N = len(grid), len(grid[0])
        num_children = 0
        disc[i][j] = self.TIME
        low_disc[i][j] = self.TIME
        self.TIME += 1
        res = False
        for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < M and 0 <= nj < N and grid[ni][nj] == 1:
                if disc[ni][nj] < 0:
                    num_children += 1
                    par[ni][nj] = (i, j)
                    res |= self.does_articulation_exist(
                        ni, nj, grid, disc, low_disc, par
                    )

                    low_disc[i][j] = min(low_disc[i][j], low_disc[ni][nj])

                    # option 1
                    if par[i][j] is None and num_children > 1:
                        res = True
                    # option2
                    elif par[i][j] is not None and disc[i][j] <= low_disc[ni][nj]:
                        res = True

                elif (ni, nj) != par[i][j]:
                    low_disc[i][j] = min(low_disc[i][j], disc[ni][nj])
        return res

    def minDays(self, grid: List[List[int]]) -> int:
        """
        This is the implementation of the Tarjan algorithm to identify the
        articulation node in a graph.

        O(MN), 54 ms, faster than 99.34%
        """
        M, N = len(grid), len(grid[0])
        disc = [[-1] * N for _ in range(M)]
        low_disc = [[-1] * N for _ in range(M)]
        par: List[List[Optional[Tuple[int, int]]]] = [[None] * N for _ in range(M)]

        num_land = 0
        num_island = 0
        art_exists = False
        # Go through the nodes one by one. For each land, try DFS to identify any articulation
        # node.
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    num_land += 1
                    if disc[i][j] < 0:
                        art_exists |= self.does_articulation_exist(
                            i, j, grid, disc, low_disc, par
                        )
                        num_island += 1
        if num_land == 0 or num_island > 1:
            return 0
        if num_land == 1 or art_exists:
            return 1
        return 2


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
