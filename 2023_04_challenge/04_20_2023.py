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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """LeetCode 662

        Put index on each node and then BFS.

        O(N), 43 ms, faster than 81.19%
        """
        queue = [(root, 0)]
        res = 1
        while queue:
            tmp = []
            for node, idx in queue:
                if node.left:
                    tmp.append((node.left, 2 * idx + 1))
                if node.right:
                    tmp.append((node.right, 2 * idx + 2))
            queue = tmp
            if queue:
                res = max(res, queue[-1][1] - queue[0][1] + 1)
        return res

        

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
