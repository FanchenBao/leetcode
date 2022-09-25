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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """LeetCode 113

        Straightforward DFS with backtracking.

        O(N), 93 ms, faster than 21.55%
        """
        res = []

        def dfs(node: Optional[TreeNode], path: List[int]) -> None:
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right:
                if sum(path) == targetSum:
                    res.append(path[:])
            else:
                if node.left:
                    dfs(node.left, path)
                if node.right:
                    dfs(node.right, path)
            path.pop()

        dfs(root, [])
        return res



sol = Solution()
tests = [
    ([4,2,1,3], [[1,2],[2,3],[3,4]]),
    ([1,3,6,10,15], [[1,3]]),
    ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.minimumAbsDifference(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
