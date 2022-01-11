# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        """LeetCode 

        This one takes longer than I'd like. But the basic idea is simple DFS.
        One tricky part is that we cannot wait until reaching an empty node to
        add to self.res. We have to add to self.res when we hit a leaf node.
        Otherwise, we will over count the path binary values.

        O(N), 36 ms, 80% ranking.
        """
        self.res = 0

        def dfs(node: Optional[TreeNode], val: int) -> None:
            cur = (val << 1) + node.val
            if not node.left and not node.right:  # leaf
                self.res += cur
                return
            if node.left:
                dfs(node.left, cur)
            if node.right:
                dfs(node.right, cur)

        dfs(root, 0)
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
