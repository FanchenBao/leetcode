# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        """LeetCode 1339

        Find the sum of each subtree.

        O(N), 429 ms, faster than 79.81% 
        """        

        def prep_sum(node: Optional[TreeNode]) -> None:
            if node:
                prep_sum(node.left)
                prep_sum(node.right)
                node.val += (node.left.val if node.left else 0) + (node.right.val if node.right else 0)

        def dfs(node: Optional[TreeNode]) -> None:
            if node:
                self.res = max(self.res, node.val * (root.val - node.val))
                dfs(node.left)
                dfs(node.right)

        prep_sum(root)
        self.res = 0
        dfs(root)
        return self.res % (10**9 + 7)


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
