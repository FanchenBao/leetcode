# from pudb import set_trace; set_trace()
from typing import List, Tuple
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """LeetCode 105

        It's quite difficult for me to reason this. But after the recursive
        relation is revealed, it's not too hard to make sense. The key observa-
        tion is that if the current preorder and inorder nodes are the same,
        that means there is no more left branch. Otherwise, we keep going to the
        left branch. Another key observation is that once inorder reaches a node
        that has already been visited, that means we need to bubble up the
        recursion to return to that previously visited node. And from there, we
        are going to head to the right branch.

        The implementation requires the tracking of the current indices on
        preorder and inorder.

        O(N), 132 ms, 52% ranking.
        """
        visited = set()
        PN, IN = len(preorder), len(inorder)

        def build(i: int, j: int) -> Tuple[TreeNode, int, int]:
            if i == PN or j == IN or inorder[j] in visited:
                return None, i, j
            root = TreeNode(val=preorder[i])
            visited.add(preorder[i])
            if preorder[i] == inorder[j]:  # no more left branch
                root.right, ni, nj = build(i + 1, j + 1)
            else:
                root.left, ni, nj = build(i + 1, j)
                # bubble up to find the previously visited root
                if nj < IN and inorder[nj] == preorder[i]:
                    root.right, nni, nnj = build(ni, nj + 1)
                    return root, nni, nnj
            return root, ni, nj
        
        root, _, _ = build(0, 0)
        return root


class Solution2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """Official solution:

        https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/
        """
        inorder_idx = {v: i for i, v in enumerate(inorder)}
        N = len(preorder)

        def build(i: int, j1: int, j2: int) -> Tuple[TreeNode, int]:
            if i == N or j1 > j2:
                return None, i
            root = TreeNode(preorder[i])
            ii = inorder_idx[preorder[i]]
            root.left, ni = build(i + 1, j1, ii - 1)  # left subtree
            root.right, ni = build(ni, ii + 1, j2)  # right subtree
            return root, ni

        root, _ = build(0, 0, N - 1)
        return root


class Solution3:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Tuple[TreeNode, int, int]:
        """No hashmap solution, but better than my original one.
        """
        N = len(preorder)

        def build(i: int, j: int, parent: int) -> TreeNode:
            if i == N or (j < N and inorder[j] == parent):
                return None, i, j
            root = TreeNode(preorder[i])
            # building left subtree ends when the inorder hits the current root
            root.left, ni, nj = build(i + 1, j, preorder[i])
            # building right subtree ends when the inorder hits the parent
            root.right, ni, nj = build(ni, nj + 1, parent)
            return root, ni, nj

        root, _, _ = build(0, 0, math.inf)
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
