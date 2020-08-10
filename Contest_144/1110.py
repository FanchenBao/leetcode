"""
07/08/2019

Initial code was written on 07/06/2019 and passed OJ. However, the code was not
the most succint. As I should know, algorithm involving tree can be designed
with great succintness. And the following is another try, after reading the
discussion section for inspiration. The magic in the code below is to set
root.left and root.right directly in the recursive call, thus any change in the
subsequent nodes can be reflected immediately on the parent node. In my old
code, I had to set up separate flags to achieve the same thing.
"""
from typing import List, Set


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res: List[TreeNode] = []
        to_delete_set: Set[int] = set(to_delete)
        self.delNodesAux(root, to_delete_set, res, True)
        return res

    def delNodesAux(self, root, to_delete, res, isRoot):
        if not root:
            return None
        # use this to indicate whether deletion happens
        deleted = root.val in to_delete
        if not deleted and isRoot:
            res.append(root)
            isRoot = False
        elif deleted:
            isRoot = True
        # important to set root.left and root.right value, because if the
        # left or right child is to be deleted, deltion can only be reflected
        # by the next two lines.
        root.left = self.delNodesAux(root.left, to_delete, res, isRoot)
        root.right = self.delNodesAux(root.right, to_delete, res, isRoot)
        # important to return value to signal whether the current node has been
        # delted.
        return None if deleted else root
