# from pudb import set_trace; set_trace()
from typing import List
import math


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """LeetCode 101

        BFS version. Kinda lazy, I don't like it.
        """
        queue = [root]
        vals = []
        while queue:
            tmp = []
            N = len(vals)
            if N > 1 and (N % 2 or vals[:N // 2] != vals[N // 2:][::-1]):
                return False
            vals.clear()
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                    vals.append(node.left.val)
                else:
                    vals.append(-101)
                if node.right:
                    tmp.append(node.right)
                    vals.append(node.right.val)
                else:
                    vals.append(-101)
            queue = tmp
        return True


class Solution2:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """Recursion

        32 ms, faster than 82.94%
        """

        def is_equal(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
            if not root1 and not root2:
                return True
            if (root1 and not root2) or (root2 and not root1):
                return False
            if root1.val != root2.val:
                return False
            return is_equal(root1.left, root2.right) and is_equal(root1.right, root2.left)

        return is_equal(root.left, root.right)
                


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
