"""
07/14/2019

This is the standard solution. It is very easy and straightforward, and it is
quite disappointing that I have to go to the discussion to realize that. I can
not believe that I wasn't able to come up with this myself yesterday. The idea
is very simple: for each root, to find the lowest common ancestor of its
deepest leaves, we need to find out the height of its left and right child
subtrees. If both substrees have the same height, then the current node is the
lca. If one substree is higher than the other, then we need to find the lca
of that higher substree by recursively calling the same function on that child
node. And that's it.

The runtime performance of the following most vanila version is very bad, as we
are calling findDepth() multiple times on the same substree. A better way to
resolve this is obviously using a memoization method (a dictionary to record
the depth of any node that has been visited already).
"""
from typing import Any


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> Any:
        if not root:
            return None
        leftDepth = self.findDepth(root.left)
        rightDepth = self.findDepth(root.right)
        if leftDepth == rightDepth:
            return root
        else:
            return (
                self.lcaDeepestLeaves(root.left)
                if leftDepth > rightDepth
                else self.lcaDeepestLeaves(root.right)
            )

    def findDepth(self, root):
        if not root:
            return 0
        else:
            return (
                max(self.findDepth(root.left), self.findDepth(root.right)) + 1
            )
