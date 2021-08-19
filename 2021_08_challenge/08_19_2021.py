# from pudb import set_trace; set_trace()
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        """LeetCode 1339

        First use DFS to obtain the sum of all subtrees that extend towards
        the leaf. This allows us to get two things. First, the sum of the
        entire tree. Second, the sum of one part of all possible cuts. Then it
        is trivial to compute the sum of the other part of the cut. Then we
        simply loop through the sums to find the max product.

        O(N) time complexity, because obtaining the subtree sum is O(N). Then
        finding the max is also O(N). 332 ms, 71% ranking.
        """
        subtree_sums = []

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            subtree_sums.append(node.val + dfs(node.left) + dfs(node.right))
            return subtree_sums[-1]

        dfs(root)
        total = subtree_sums.pop()
        return max(s * (total - s) for s in subtree_sums) % 1000000007


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
