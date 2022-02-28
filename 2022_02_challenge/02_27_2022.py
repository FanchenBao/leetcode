# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """LeetCode 662

        BFS with indices for each node.

        O(N), 44 ms, 90% ranking.
        """
        queue = [(root, 1)]
        res = 0
        while queue:
            temp = []
            res = max(res, queue[-1][1] - queue[0][1] + 1)
            for node, idx in queue:
                if node.left:
                    temp.append((node.left, idx * 2))
                if node.right:
                    temp.append((node.right, idx * 2 + 1))
            queue = temp
        return res
        

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
