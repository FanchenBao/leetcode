# from pudb import set_trace; set_trace()
from typing import List
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """LeetCode 450

        This is a classic. I have done it before, and learned it from my algo
        class. But still, this problem is challenging because of all the cases
        that need to be considered. My first attempt failed to consider the
        situation where the most left node of the current node's right subtree
        can itself have a right subtree. This means, we have to run the delete
        function recursively on the left most node of the current node's right
        substree.

        O(logN), 77 ms, 39% ranking.
        """
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right:
                return root.left
            if not root.right.left:
                root.right.left = root.left
                return root.right
            subpar = root.right
            subcur = root.right.left
            while subcur.left:
                subpar = subcur
                subcur = subcur.left
            root.val, subcur.val = subcur.val, root.val
            subpar.left = self.deleteNode(subpar.left, key)
        return root

# sol = Solution()
# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
