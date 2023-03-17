# from pudb import set_trace; set_trace()
from typing import List
import math


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """LeetCode 106

        Go from right to left with postorder, because each element is the
        current root of the subtree. Once we identify the current root, we
        search in inorder for its position, and split inorder into left and
        right subtree. We continue with the right subtree first, and then left
        subtree.

        O(N + logN), 46 ms, faster than 99.62%
        """
        idx_map = {v: i for i, v in enumerate(inorder)}
        self.idx = len(postorder) - 1

        def helper(lo: int, hi: int) -> Optional[TreeNode]:
            if lo > hi:
                return None
            root = TreeNode(val=postorder[self.idx])
            root_idx = idx_map[postorder[self.idx]]
            self.idx -= 1
            if lo != hi:
                root.right = helper(root_idx + 1, hi)
                root.left = helper(lo, root_idx - 1)
            return root

        return helper(0, len(inorder) - 1)
        

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
