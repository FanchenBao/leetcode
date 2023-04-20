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
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        """LeetCode 1372

        DFS, and keep counting the zig zag path. Each time the child's direction
        is the same as the parent's, reset the count. Record the max count at
        each node.

        O(N), 381 ms, faster than 80.95%
        """
        self.res = 0

        def dfs(node: TreeNode, pre_dir: str, cur_len: int) -> None:
            cur_len += 1
            self.res = max(self.res, cur_len)
            if node.left:
                dfs(node.left, 'l', cur_len if pre_dir != 'l' else 0)
            if node.right:
                dfs(node.right, 'r', cur_len if pre_dir != 'r' else 0)

        dfs(root, '', -1)
        return self.res
        

# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
