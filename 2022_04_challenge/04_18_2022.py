# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """LeetCode 230

        In-order traversal, keep track of the position of the current node
        being visited.

        O(K), 55 ms, 82.59% 
        """
        self.k = k

        def helper(node: Optional[TreeNode]) -> int:
            if not node:
                return -1
            lv = helper(node.left)
            if lv >= 0:
                return lv
            self.k -= 1
            if self.k == 0:
                return node.val
            return helper(node.right)

        return helper(root)

        

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
