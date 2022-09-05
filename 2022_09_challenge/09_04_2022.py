# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        """LeetCode 987

        Took a double-take to really understand what the problem wants, but
        once that is settled the solution is very straightforward.

        63 ms, faster than 26.21%
        """
        res = defaultdict(list)

        def dfs(node: Optional[TreeNode], row: int, col: int) -> None:
            if node:
                res[col].append((row, node.val))
                dfs(node.left, row + 1, col - 1)
                dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)
        return [[tup[1] for tup in sorted(res[k])] for k in sorted(res)]


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
