# from pudb import set_trace; set_trace()
from typing import List, Tuple
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """LeetCode 1026.

        At each node, we compute the min and max of its left and right subtree,
        if they exit. Then, we can compute the max diff involving the current
        node using the min max from the left and right subtree (i.e. children).
        We update the global diff. Finally, we return the min and max of the
        tree rooted at the current node.

        O(N), 44 ms, 39% ranking.
        """
        self.res = -1

        def helper(node: Optional[TreeNode]) -> Tuple[int, int]:
            cur_min, cur_max = node.val, node.val
            if node.left:
                left_min, left_max = helper(node.left)
                cur_min = min(cur_min, left_min)
                cur_max = max(cur_max, left_max)
                self.res = max(
                    self.res,
                    abs(node.val - left_min),
                    abs(node.val - left_max),
                )
            if node.right:
                right_min, right_max = helper(node.right)
                cur_min = min(cur_min, right_min)
                cur_max = max(cur_max, right_max)
                self.res = max(
                    self.res,
                    abs(node.val - right_min),
                    abs(node.val - right_max),
                )
            return cur_min, cur_max

        helper(root)
        return self.res


class Solution2:
    def maxAncestorDiff(
        self,
        root: Optional[TreeNode],
        path_min: int = math.inf,
        path_max: int = -math.inf,
    ) -> int:
        """This is the good solution from a year ago. The idea is to traverse
        each path from root to leaf. Along the way, we keep an eye on the min
        and max, and keep track of their difference. After we go through all
        paths, the max such min-max diff is the result
        """
        if not root:
            return path_max - path_min
        cmin, cmax = min(path_min, root.val), max(path_max, root.val)
        return max(
            self.maxAncestorDiff(root.left, cmin, cmax),
            self.maxAncestorDiff(root.right, cmin, cmax),
        )
        

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
