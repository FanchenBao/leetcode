# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        """LeetCode 623

        BFS to find the parent row.

        O(N), 60 ms, faster than 89.85%
        """
        if depth == 1:
            return TreeNode(val=val, left=root)
        queue = [root]
        depth -= 1
        while queue:
            temp = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            depth -= 1
            if not depth:
                break
            queue = temp
        for node in queue:
            temp_left, temp_right = node.left, node.right
            node.left = TreeNode(val=val, left=temp_left)
            node.right = TreeNode(val=val, right=temp_right)
        return root



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
