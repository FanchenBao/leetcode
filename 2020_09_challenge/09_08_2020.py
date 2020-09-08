# from pudb import set_trace; set_trace()
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, node: TreeNode, bstr: str) -> None:
        if not node:
            return 0
        v_str: str = str(node.val)
        if node.left is None and node.right is None:
            return int(bstr + v_str, 2)
        return self.traverse(node.left, bstr + v_str) + self.traverse(node.right, bstr + v_str)

    def sumRootToLeaf(self, root: TreeNode) -> int:
        """Pass OJ. Standard solution."""
        return self.traverse(root, '')
