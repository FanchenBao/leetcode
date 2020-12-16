# from pudb import set_trace; set_trace()
from typing import List
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def isValidBST(self, root: TreeNode) -> bool:
        """Straightforward inorder search, and compare whether the current node
        value is larger than the previous one.

        O(N), 40 ms, 86% ranking.
        """
        self.pre = -math.inf

        def inorder(node: TreeNode) -> bool:
            if not node:
                return True
            if not inorder(node.left):
                return False
            if node.val <= self.pre:
                return False
            self.pre = node.val
            return inorder(node.right)

        return inorder(root)


class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        """This is the smart recursion solution. Each node must have a min-max
        limit. If on the left branch, the min requirement is the same as the
        parent, but the max requirement is the parent. If on the right branch,
        the max requirement is the same as the parent, but the min requirement
        it the parent.

        O(N), 44 ms, 65% ranking.
        """

        def dfs(node: TreeNode, min_node: TreeNode, max_node: TreeNode) -> bool:
            if not node:
                return True
            if not min_node.val < node.val < max_node.val:
                return False
            return dfs(node.left, min_node, node) and dfs(node.right, node, max_node)

        return dfs(root, TreeNode(val=-math.inf), TreeNode(val=math.inf))


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
