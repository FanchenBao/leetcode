# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def minDepth(self, root: TreeNode) -> int:
        """A BFS shall suffice"""
        queue = [(TreeNode(left=root), 0)]
        for node, lvl in queue:
            if node.left:
                queue.append((node.left, lvl + 1))
            if node.right:
                queue.append((node.right, lvl + 1))
            if not node.left and not node.right:
                break
        return lvl


class Solution2:
    def minDepth(self, root: TreeNode) -> int:
        """Use recursion"""
        if not root:
            return 0
        if not root.left and not root.right:  # leaf
            return 1
        elif not root.left and root.right:
            return self.minDepth(root.right) + 1
        elif not root.right and root.left:
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


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
