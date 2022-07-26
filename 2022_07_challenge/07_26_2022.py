# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """LeetCode 236

        The return value of dfs is 00 => not found, 01 => found q,
        10 => found p, and 11 => found both. Thus, the check is for 3.

        O(N), 167 ms, faster than 9.55% It's very slow. I don't know why
        """
        self.res = None

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            cur = l | r | (2 if node == p else (1 if node == q else 0))
            if cur == 3 and self.res is None:
                self.res = node
            return cur

        dfs(root)
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
