# from pudb import set_trace; set_trace()
from typing import List

Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, node: TreeNode, is_left: bool) -> int:
        if not node:
            return 0
        is_leaf = node.left is None and node.right is None
        s = self.helper(node.left, True) + self.helper(node.right, False)
        return s if not is_leaf else node.val if is_left else 0

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self.helper(root, False) if root else 0
