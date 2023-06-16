# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """LeetCode 1161

        BFS, O(N), 292 ms, faster than 89.65%
        """
        res = 1
        max_sum = -math.inf
        queue = [root]
        lvl = 1
        while queue:
            tmp = []
            cur_sum = 0
            for node in queue:
                cur_sum += node.val
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if max_sum < cur_sum:
                res = lvl
                max_sum = cur_sum
            queue = tmp
            lvl += 1
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
