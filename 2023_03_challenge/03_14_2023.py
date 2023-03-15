# from pudb import set_trace; set_trace()
from typing import List
import math


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """LeetCode 129

        DFS. O(N), 29 ms, faster than 84.93%
        """
        self.res = 0

        def dfs(node: Optional[TreeNode], val: int) -> None:
            if not node:
                return
            val = val * 10 + node.val
            if not node.left and not node.right:  # leaf
                self.res += val
                return
            dfs(node.left, val)
            dfs(node.right, val)

        dfs(root, 0)
        return self.res

        


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
