# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        """This is a very standard DFS problem in Tree. We basically need to 
        find the sum of the tree and the count of the nodes, both are easily
        done via dfs.

        O(N), 66 ms, faster than 50.20%
        """
        self.res = 0

        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            if not node:
                return 0, 0
            ls, lc = dfs(node.left)
            rs, rc = dfs(node.right)
            s = ls + rs + node.val
            c = lc + rc + 1
            if node.val == s // c:
                self.res += 1
            return s, c

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
