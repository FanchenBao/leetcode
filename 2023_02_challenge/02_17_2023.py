# from pudb import set_trace; set_trace()
from typing import List
import math


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        """LeetCode 783

        Every subtree returns the max and min value. Compare with the root val
        with left max and right min.

        O(N), 30 ms, faster than 85.90%
        """
        self.res = math.inf

        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            rmax = lmin = node.val
            if node.left:
                lmax, lmin = dfs(node.left)
                self.res = min(self.res, node.val - lmax)
            if node.right:
                rmax, rmin = dfs(node.right)
                self.res = min(self.res, rmin - node.val)
            return rmax, lmin

        dfs(root)
        return self.res


class Solution2:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        """Inorder traversal
        """
        self.res = math.inf
        self.pre = None

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            dfs(node.left)
            if self.pre:
                self.res = min(self.res, node.val - self.pre.val)
            self.pre = node
            dfs(node.right)

        dfs(root)
        return self.res


# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
