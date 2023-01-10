# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """LeetCode 144
        
        Iterative method

        O(N), 27 ms, faster than 95.77%
        """
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
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
