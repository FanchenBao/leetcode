# from pudb import set_trace; set_trace()
from typing import List, Tuple
from collections import deque



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """LeetCode 543

        At each node, we find out the longest path on its left and right
        branches. The sume of these two lengths is the longest path that goes
        through the node. We record this, and return the longer of the two paths
        as the longest branch involving the current node.

        O(N) time, 63 ms, 25% ranking.
        """
        self.res = 0

        def helper(node) -> int:
            lmax = (helper(node.left) + 1) if node.left else 0
            rmax = (helper(node.right) + 1) if node.right else 0
            self.res = max(self.res, lmax + rmax)
            return max(lmax, rmax)

        helper(root)
        return self.res


        

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
