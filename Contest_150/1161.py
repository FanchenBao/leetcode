#! /usr/bin/env python3
from typing import List

"""08/23/2019

Solution1:

BFS. I use a simple list as queue. I have to keep track the number of nodes on
each level to indicate when the next level begins. For each level, simply sum
all the node's values. We have to go through the entire tree to find the answer,
so the complexity is O(n). This solution clocked in at 320 ms, 74%

Solution2:

DFS. After reading the discussion, I realized that DFS is also possible to solve
this problem. All we need to do is to traverse the tree in DFS fashion, note
the level each node is at and sum up the node values of the same level. This
solution clocked in at 380 ms, 21%.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def maxLevelSum(self, root: TreeNode) -> int:
        bfs: List[TreeNode] = [root]
        curr_sum, max_sum = 0, 0
        res_lvl, lvl = 0, 1
        curr_lvl_nodes, next_lvl_nodes = 1, 0
        for node in bfs:
            curr_lvl_nodes -= 1
            curr_sum += node.val
            if node.left is not None:  # push next level's nodes into queue
                bfs.append(node.left)
                next_lvl_nodes += 1
            if node.right is not None:
                bfs.append(node.right)
                next_lvl_nodes += 1
            if curr_lvl_nodes == 0:  # current level ends, do the analysis
                if curr_sum > max_sum:
                    max_sum = curr_sum
                    res_lvl = lvl
                lvl += 1  # prepare for next level
                curr_lvl_nodes = next_lvl_nodes
                next_lvl_nodes = 0
                curr_sum = 0
        return res_lvl


class Solution2:
    def maxLevelSum(self, root: TreeNode) -> int:
        level_sums: List[int] = []
        self.dfs(root, 1, level_sums)
        max_sum, res_lvl = 0, 0
        for i, ls in enumerate(level_sums):
            if ls > max_sum:
                max_sum = ls
                res_lvl = i + 1
        return res_lvl

    def dfs(self, root: TreeNode, lvl: int, level_sums: List[int]) -> None:
        """ Traverse throughout the tree and record sums at each level """
        if root is None:
            return
        if lvl > len(level_sums):
            level_sums.append(0)
        level_sums[lvl - 1] += root.val
        self.dfs(root.left, lvl + 1, level_sums)
        self.dfs(root.right, lvl + 1, level_sums)
