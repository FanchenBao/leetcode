# from pudb import set_trace; set_trace()
from typing import List


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> Node:
        """This method is very straightforward. First, we check whether all
        values in the grid are the same, and then do recursion on four subgrids

        O(NlogN), 108 ms, 92% ranking.

        UPDATE: better method to check if all values are the same in the grid

        Ref: https://leetcode.com/problems/construct-quad-tree/discuss/195855/Python-very-simple-recursive-solution-beats-97
        """

        def dfs(x1: int, y1: int, x2: int, y2: int) -> Node:
            """(x1, y1) is the top left corner.
            (x2, y2) is the bottom right corner.
            """
            if all(grid[i][j] == grid[y1][x1] for i in range(y1, y2 + 1) for j in range(x1, x2 + 1)):
                return Node(
                    val=grid[y1][x1],
                    isLeaf=True,
                    topLeft=None,
                    topRight=None,
                    bottomLeft=None,
                    bottomRight=None,
                )
            return Node(
                val=True,
                isLeaf=False,
                topLeft=dfs(x1, y1, (x2 - x1 + 1) // 2 + x1 - 1, (y2 - y1 + 1) // 2 + y1 - 1),
                topRight=dfs((x2 - x1 + 1) // 2 + x1, y1, x2, (y2 - y1 + 1) // 2 + y1 - 1),
                bottomLeft=dfs(x1, (y2 - y1 + 1) // 2 + y1, (x2 - x1 + 1) // 2 + x1 - 1, y2),
                bottomRight=dfs((x2 - x1 + 1) // 2 + x1, (y2 - y1 + 1) // 2 + y1, x2, y2),
            )

        return dfs(0, 0, len(grid) - 1, len(grid) - 1)

        


# sol = Solution()
# tests = [
#     ([4,2,1,3], [[1,2],[2,3],[3,4]]),
#     ([1,3,6,10,15], [[1,3]]),
#     ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
# ]

# for i, (arr, ans) in enumerate(tests):
#     res = sol.minimumAbsDifference(arr)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
