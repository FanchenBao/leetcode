# from pudb import set_trace; set_trace()
from typing import List, Dict, Optional
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_heights(self, node: Optional[TreeNode]) -> int:
        if not node:
            return -1
        h = 1 + max(self.get_heights(node.left), self.get_heights(node.right))
        self.heights[node.val] = h
        return h

    def after_removal(
        self, node: Optional[TreeNode], impact: bool, other_height: int
    ) -> None:
        """
        Find the height of the binary tree after the current node is removed.

        other_height is the second largest height when the binary tree first
        bifurcates. In other words, other_height will take over if the removal
        causes the original max height to be smaller

        impact indicates whether the current node is on the path that determines
        the max height. If not, removing the current node will not result in
        any change to the max height
        """
        if not node:
            return
        if not impact:
            self.heights_after_removal[node.val] = self.total_height
            self.after_removal(node.left, impact, other_height)
            self.after_removal(node.right, impact, other_height)
            return
        lh = self.heights[node.left.val] if node.left else -1
        rh = self.heights[node.right.val] if node.right else -1
        next_other_height = other_height
        if node.left and node.right and other_height < 0:
            next_other_height = self.total_height - max(lh, rh) + min(lh, rh)
        if lh == rh:
            self.heights_after_removal[node.val] = max(
                other_height, self.total_height - rh - 2
            )
            self.after_removal(node.left, False, next_other_height)
            self.after_removal(node.right, False, next_other_height)
        elif lh < rh:
            self.heights_after_removal[node.val] = max(
                other_height, self.total_height - rh - 2
            )
            self.after_removal(node.left, False, next_other_height)
            self.after_removal(node.right, True, next_other_height)
        else:
            self.heights_after_removal[node.val] = max(
                other_height, self.total_height - lh - 2
            )
            self.after_removal(node.left, True, next_other_height)
            self.after_removal(node.right, False, next_other_height)

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        """
        This solution originates from the hint. We go through the tree once to
        obtain the heights at all the nodes.

        We then go through it one more time to find out the max height of the
        tree after each node is removed.

        Then we can easily obtain the answer when querying.
        """
        self.heights: Dict[int, int] = {}
        self.heights_after_removal: Dict[int, int] = {}
        self.total_height = self.get_heights(root)
        self.after_removal(root, True, -1)
        return [self.heights_after_removal[q] for q in queries]


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
