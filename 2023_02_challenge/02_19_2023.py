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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """LeetCode 103

        BFS, 25 ms, faster than 97.68%
        """
        if not root:
            return []
        queue = [root]
        res = []
        left_to_right = 1
        while queue:
            tmp = []
            res.append([])
            for node in queue:
                res[-1].append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp
            if left_to_right < 0:
                res[-1] = res[-1][::-1]
            left_to_right *= -1
        return res


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
