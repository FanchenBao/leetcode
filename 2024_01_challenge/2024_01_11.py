# from pudb import set_trace; set_trace()
from typing import List, Optional, Tuple
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """
        LeetCode 1026

        DFS to find the min and max of each subtree, compute the absolute
        difference between them and the subtree root's value. Maintain the
        max of such absolute difference.

        O(N), 38 ms, faster than 85.36%
        """
        self.res = 0

        def find_min_max(node: TreeNode) -> Tuple[int, int]:
            if not node.left and not node.right:
                # handle the leaf
                return node.val, node.val
            c_min, c_max = node.val, node.val
            if node.left:
                l_min, l_max = find_min_max(node.left)
                c_min, c_max = min(l_min, c_min), max(l_max, c_max)
                self.res = max(self.res, abs(l_min - node.val), abs(l_max - node.val))
            if node.right:
                r_min, r_max = find_min_max(node.right)
                c_min, c_max = min(r_min, c_min), max(r_max, c_max)
                self.res = max(self.res, abs(r_min - node.val), abs(r_max - node.val))
            return c_min, c_max

        find_min_max(root)
        return self.res






sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
