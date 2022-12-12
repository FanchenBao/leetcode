# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """LeetCode 124

        There are only three possible paths. Path go down left, path go down
        right, or path from left, passing root, go down right.

        Thus, at each node, we need to find the max path sum on left and right,
        then get the max of all the options.

        max_l + node.val --> path go down left
        max_r + node.val --> path go down right
        max_l + max_r + node.val --> path from left to right
        node.val --> path is just the root (don't forget this!)

        O(N), 241 ms, faster than 10.93% 
        """
        self.res = -math.inf

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            max_l = dfs(node.left)
            max_r = dfs(node.right)
            max_path = max([max_l + node.val, max_r + node.val, node.val])
            self.res = max([self.res, max_path, max_l + max_r + node.val])
            return max_path

        dfs(root)
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
