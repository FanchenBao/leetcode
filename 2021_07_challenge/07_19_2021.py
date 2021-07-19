# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def __init__(self):
        self.lca = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """LeetCode 235

        I have done this before, probably less than a month ago. The solution
        used here is from either the official solution or someone's solution.
        It's very simple. We basically check how many nodes we can find in the
        current tree that match either p or q. If the value is two, that means
        the current node is a common ancestor. We then check whether LCA has
        been set before. If not, then the current common ancestor is the LCA.
        Otherwise, LCA has been found already and we do nothing.

        O(N), 92 ms, 26% ranking.
        """
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            count = dfs(node.left) + dfs(node.right) + (node == p or node == q)
            if count == 2 and self.lca is None:
                self.lca = node
            return count

        dfs(root)
        return self.lca


class Solution2:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """It turns out I have not done this exact problem before. I have,
        however, done the more generic version of this problem (LeetCode 236),
        and the solution here is for the generic version.

        This problem uses a BST, which shall allow us to pick which branch to
        go to. Also, I am reverting back to
        the official solution of LeetCode 236, which returns boolean value.

        80 ms
        """

        self.lca = None

        def dfs(node: TreeNode) -> int:
            if not node:
                return False
            if p.val < node.val and q.val < node.val:
                found_left = dfs(node.left)
                found_right = False
            elif p.val > node.val and q.val > node.val:
                found_left = False
                found_right = dfs(node.right)
            else:
                found_left = dfs(node.left)
                found_right = dfs(node.right)
            found_self = node == p or node == q
            if found_left + found_right + found_self == 2:
                self.lca = node
            return found_left or found_right or found_self

        dfs(root)
        return self.lca


class Solution3:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """This is from the official solution, which reveals a very simple fact
        that in a BST, if p.val < node.val < q.val, then node is automatically
        the LCA.
        """
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
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
