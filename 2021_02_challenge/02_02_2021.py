# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        """A straightforward solution. Since the tree is a binary search tree,
        we can compare the range with the root to determine which branch we
        need to pursue. This can cut a lot of run time. The complicated case is
        when the range spans the root. In this case, we need to split into
        two branches, instead of going down only one.

        O(N), 88 ms, 5% ranking.
        """

        if low > high:
            return None
        if not root:
            return None
        if low > root.val:
            return self.trimBST(root.right, low, high)
        if high < root.val:
            return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, root.val - 1)
        root.right = self.trimBST(root.right, root.val + 1, high)
        return root


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
