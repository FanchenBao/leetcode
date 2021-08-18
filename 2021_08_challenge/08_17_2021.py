# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """LeetCode 1448

        A simple DFS suffices. We keep track of the max value in each DFS
        path. If the current node is larger or equal to the max, increment the
        result and update the max value.

        O(N), 232 ms, 89% ranking.
        """
        self.res = 0

        def dfs(node: TreeNode, cur_max: int) -> None:
            if not node:
                return
            if node.val >= cur_max:
                self.res += 1
                cur_max = node.val
            dfs(node.left, cur_max)
            dfs(node.right, cur_max)

        dfs(root, root.val)
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
