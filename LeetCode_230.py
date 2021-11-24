# from pudb import set_trace; set_trace()
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """Inorder traversal.

        O(H + K), where N is the total number of nodes.
        59 ms, 30% rankinng.
        """
        self.k = k

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return -1
            lres = dfs(node.left)
            if lres >= 0:
                return lres
            self.k -= 1
            if self.k == 0:
                return node.val
            rres = dfs(node.right)
            if rres >= 0:
                return rres
            return -1

        return dfs(root)

        

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
