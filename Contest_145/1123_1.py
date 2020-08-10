"""
07/14/2019

I didn't solve this problem during the contest, due to some confusion about
what lowest common ancestor actually meant. I solved it by myself earlier
today using quite dumb method: finding each leaf and recording its path.
If a deeper leaf is found, the previously found paths are discarded. If a leaf
of the same depth is found, we compare the two paths and keep the common path.
Eventually, we return the end of the common path.

This is a terrible solution, but surprisingly it passed OJ. I will write about
a more standard solution (after reading the discussion in another file)
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        commmonPath: List[List[TreeNode]] = [[]]
        self.helper(root, commmonPath, [], 0, [0])
        return commmonPath[0][-1]

    def helper(self, root, commmonPath, currPath, depth, maxDepth):
        currPath.append(root)
        if (not root.left) and (not root.right):  # current node is leaf
            if depth > maxDepth[0]:
                maxDepth[0] = depth
                commmonPath[0] = currPath[:]
            elif depth == maxDepth[0]:
                i = 0
                while i < len(commmonPath[0]):
                    if commmonPath[0][i] != currPath[i]:
                        break
                    i += 1
                commmonPath[0] = commmonPath[0][:i]
        else:
            if root.left:
                self.helper(
                    root.left, commmonPath, currPath, depth + 1, maxDepth
                )
            if root.right:
                self.helper(
                    root.right, commmonPath, currPath, depth + 1, maxDepth
                )
        currPath.pop()
