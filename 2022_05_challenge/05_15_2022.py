# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        """LeetCode 1302

        BFS

        O(N), 360 ms, faster than 24.59%
        """
        queue = [root]
        res = 0
        while queue:
            temp = []
            ts = 0
            for node in queue:
                ts += node.val
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
            res = ts
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
