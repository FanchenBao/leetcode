# from pudb import set_trace; set_trace()
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        """LeetCode 814

        At each node, we prune the left and right first. The return of the
        pruning is None if the subtree needs to be deleted. Otherwise we return
        the root of the subtreee.

        If a node's left and right subtrees both do not contain 1 (i.e. both
        the left and right subtrees are removed), we check whether the node
        itself is a 1. If it is, we do not remove it. Otherwise, we remove it.

        O(N), 32 ms, 63% ranking.
        """
        if not root:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        return None if not root.left and not root.right and root.val != 1 else root
        

# sol = Solution3()
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
