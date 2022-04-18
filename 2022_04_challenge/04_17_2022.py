# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        """LeetCode 897

        Use a global variable within the function to record the current pos
        of the new tree. This avoids the need to create a sorted array first.

        39 ms, faster than 65.11%
        """
        self.dummy = TreeNode()
        self.node = self.dummy

        def helper(node: TreeNode) -> None:
            if node:
                helper(node.left)
                self.node.right = TreeNode(node.val)
                self.node = self.node.right
                helper(node.right)

        helper(root)
        return self.dummy.right


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
