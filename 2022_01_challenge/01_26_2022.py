# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        """LeetCode 

        Obtain the sorted list from each binary search tree, and then perform
        merge sort.

        O(N), 340 ms, 76% ranking.

        UPDATE: user heapq.merge to perform the merge sort
        """

        def dfs(node: Optional[TreeNode], sorted_lst: List[int]):
            if node:
                dfs(node.left, sorted_lst)
                sorted_lst.append(node.val)
                dfs(node.right, sorted_lst)

        s1, s2 = [], []
        dfs(root1, s1)
        dfs(root2, s2)
        return list(heapq.merge(s1, s2))



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
