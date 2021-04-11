# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        """LeetCode 1302

        BFS, return the sum of the last level

        O(N), 88ms, 86% ranking.
        """
        queue, res = [root], 0
        while queue:
            tlst, tres = [], 0
            for node in queue:
                tres += node.val
                if node.left:
                    tlst.append(node.left)
                if node.right:
                    tlst.append(node.right)
            queue, res = tlst, tres  # update
        return res


class Solution2:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        """The smart BFS by lee215.

        https://leetcode.com/problems/deepest-leaves-sum/discuss/463239/JavaC%2B%2BPython-Level-Traversal

        It's the same BFS, but implemented as a level-traversal. We end up with
        the nodes in the last level, but we do not do any computation while at
        each level. Also, it has good use of list comprehension.
        """
        q = [root]
        while q:
            pre, q = q, [child for n in q for child in [n.left, n.right] if child]
        return sum(n.val for n in pre)

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
