# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def convertBST(self, root: TreeNode) -> TreeNode:
        """It took quite a few iterations to come up with the correct recursion.
        The main obstacle was that the return value from a node was unclear. It
        should be that we always return the original sum of all the values in
        the subtree (including the subtree node). The workflow is like this:
        Each node's altered value equals its parent contribution plus its right
        child's contribution plus itself (i.e. pcont + rcont + node.val). And
        the return value of a node is its updated value minus parent
        contribution plus left child's contribution (i.e. node.val - pcont +
        lcont). This is essentially the sum of lcont + rcont + original node.val

        O(N), 68 ms, 99% ranking.
        """

        def dfs(node: TreeNode, pcont: int) -> int:
            if not node:
                return 0
            rcont = dfs(node.right, pcont)
            node.val += pcont + rcont
            lcont = dfs(node.left, node.val)
            return node.val - pcont + lcont

        dfs(root, 0)
        return root


class Solution2:
    def __init__(self):
        self.total = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        """This is the official recursion solution, which uses a counter to keep
        track of the sum of the nodes visited. Since we are visiting the right
        branch first, the sum is always the largest nodes encountered so far.

        O(N), 84 ms, 58% ranking.
        """
        if root:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
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
