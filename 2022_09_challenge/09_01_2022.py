# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """LeetCode 1448

        O(N), 305 ms, faster than 78.78% 
        """
        self.res = 0

        def dfs(node: Optional[TreeNode], cur_max: int) -> None:
            if node:
                if cur_max <= node.val:
                    self.res += 1
                    cur_max = node.val
                dfs(node.left, cur_max)
                dfs(node.right, cur_max)

        dfs(root, -math.inf)
        return self.res

        

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
