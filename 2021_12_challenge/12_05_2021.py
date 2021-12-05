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
    def rob(self, root: Optional[TreeNode]) -> int:
        """LeetCode 337

        I have seen improvements in this one. This is the correct solution.
        However, I did hit a little bit obstacle when one of the test cases
        failed. The problem was that when the current node is not robbed, we do
        not have to rob its children. In other words, the max profit from not
        robbing the current node should be the max profit of its children,
        regardless of whether the children are robbed or not.

        O(N), 64 ms, 29% ranking.
        """
        Ret = namedtuple('Ret', 'yes, no')

        def helper(node: Optional[TreeNode]) -> Tuple[int, int]:
            if not node:
                return Ret(0, 0)
            left = helper(node.left)
            right = helper(node.right)
            return Ret(node.val + left.no + right.no, max(left) + max(right))

        return max(helper(root))


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
