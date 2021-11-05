# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """LeetCode 144

        32 ms, 68% ranking.
        """
        if not root:
            return []
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        return [root.val] + left + right


class Solution2:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        28 ms, 87% ranking.
        """
        res = []

        def dfs(node: Optional[TreeNode]) -> None:
            if node:
                res.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return res

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
