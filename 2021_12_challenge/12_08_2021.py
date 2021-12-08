# from pudb import set_trace; set_trace()
from typing import List
from collections import namedtuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        """LeetCode 563

        Simple post-order traversal.

        O(N), 54 ms, 79% ranking
        """
        self.res = 0

        def helper(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            sum_l = helper(node.left)
            sum_r = helper(node.right)
            self.res += abs(sum_r - sum_l)
            return sum_l + sum_r + node.val

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
