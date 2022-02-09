# from pudb import set_trace; set_trace()
from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution1:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        """Not a difficult problem. All we need to do is DFS while keeping
        track of the height. As long as we DFS with left branch first, the very
        first node encountered on a lower level must be the left most leaf.

        O(N), 69 ms, 30% ranking.
        """
        left_leaf = [0, -1]
        
        def dfs(node, height) -> None:
            if not node.left and not node.right and height > left_leaf[1]:  # leaf
                left_leaf[0] = node.val
                left_leaf[1] = height
                return
            if node.left:
                dfs(node.left, height + 1)
            if node.right:
                dfs(node.right, height + 1)

        dfs(root, 0)
        return left_leaf[0]


class Solution2:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        """BFS. It is easier to implement and understand then DFS.

        O(N), 41 ms, 83% ranking.
        """
        res = 0
        queue = [root]
        while queue:
            temp = []
            res = queue[0].val
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
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
