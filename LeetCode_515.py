# from pudb import set_trace; set_trace()
from typing import List
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        """Simple BFS

        Pay attention to the edge case when root is empty!

        O(N), 90ms, 11% ranking
        """
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            temp = []
            res.append(-math.inf)
            for node in queue:
                res[-1] = max(res[-1], node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
        return res


class Solution2:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        """DFS, inspired by:

        https://leetcode.com/problems/find-largest-value-in-each-tree-row/discuss/98971/9ms-JAVA-DFS-solution

        O(N), 48 ms, 79% ranking.
        """
        res = []

        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if node:
                if len(res) == depth:
                    res.append(node.val)
                else:
                    res[depth] = max(res[depth], node.val)
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)

        dfs(root, 0)
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
