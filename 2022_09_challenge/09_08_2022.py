# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """LeetCode 94

        O(N), 62 ms, faster than 13.79%
        """
        res = []

        def dfs(node: Optional[TreeNode]) -> None:
            if node:
                dfs(node.left)
                res.append(node.val)
                dfs(node.right)

        dfs(root)
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
