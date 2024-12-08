# from pudb import set_trace; set_trace()
from typing import List, Dict, Optional
import math
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.cur_max_height: int = 0
        self.max_height_after_removal: Dict[int, int] = defaultdict(int)

    def bfs(self, node: Optional[TreeNode], lvl: int, is_ltr: bool) -> None:
        if not node:
            return
        self.max_height_after_removal[node.val] = max(
            self.max_height_after_removal[node.val], self.cur_max_height
        )
        self.cur_max_height = max(self.cur_max_height, lvl)
        if is_ltr:
            self.bfs(node.left, lvl + 1, True)
            self.bfs(node.right, lvl + 1, True)
        else:
            self.bfs(node.right, lvl + 1, False)
            self.bfs(node.left, lvl + 1, False)

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        """
        This solution comes from the official solution. We find the height of
        the tree after removing each node. We store the results and can easily
        query it.

        To find the height after a node is removed, we need to do two rounds of
        traversals. First, we do left to right and keep track of the height.
        This tells us the max height before a node is visited. This height
        represents the left trees.
        Then, we do right to left and obtain the max height before the same
        node is visited. This height represents the right trees.

        Thus, the max height when the node is removed is the bigger of the
        left tree height and right tree height.

        O(N), 380 ms, faster than 21.36%
        """
        self.bfs(root, 0, True)
        self.cur_max_height = 0  # reset before second round of bfs
        self.bfs(root, 0, False)
        return [self.max_height_after_removal[q] for q in queries]


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
