# from pudb import set_trace; set_trace()
from typing import List
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """The idea is to create two types of max path sum at any root. One
        type is the max path sum that must pass the root. This is the sum that
        will return to the parent. This sum is important, because if any max
        path sum does not pass through the root, it is useless for the parent.
        For instance, if the actual max path sum is an arch that goes from left
        to root to right, this path cannot be incorporated with the parent.

        The second type is the actual max path sum, which will be computed as
        the max between the rooted max path sum and the arch max path sum.
        The result will be checked at each node, because the actual max path
        sum can be present anywhere in the tree.

        O(N), 84 ms, 80% ranking.
        """
        self.res = -math.inf

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return -math.inf
            max_left = dfs(node.left)
            max_right = dfs(node.right)
            max_root_path = max(node.val, node.val + max_left, node.val + max_right)
            self.res = max(
                self.res,
                max_left + node.val + max_right,  # the arch
                max_root_path,  # rooted path
            )
            return max_root_path

        dfs(root)
        return self.res


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
