# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """LeetCode 112

        O(N), 95 ms, faster than 16.17%
        """

        def dfs(node: Optional[TreeNode], cur_sum: int) -> bool:
            if not node:
                return False
            cur_sum += node.val
            if not node.left and not node.right:
                return cur_sum == targetSum
            return dfs(node.left, cur_sum) or dfs(node.right, cur_sum)

        return dfs(root, 0)

        

# sol = Solution()
# tests = [
#     ([4,2,1,3], [[1,2],[2,3],[3,4]]),
#     ([1,3,6,10,15], [[1,3]]),
#     ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
# ]

# for i, (arr, ans) in enumerate(tests):
#     res = sol.minimumAbsDifference(arr)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
