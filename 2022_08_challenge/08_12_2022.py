# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """LeetCode 235

        We can definitely solve this using the method as if the tree is a
        regular binary tree. However, the tree being BST means that we can use
        additional info contained in the values to simplify the search process.
        Whenever a node sits between the p and q values, the node must be the
        LCA.

        O(logN), 163 ms, faster than 12.64%
        """
        self.res = None
        if p.val > q.val:
            p, q = q, p

        def dfs(node) -> None:
            if node:
                if p.val <= node.val <= q.val:
                    self.res = node
                elif node.val > q.val:
                    dfs(node.left)
                elif node.val < p.val:
                    dfs(node.right)

        dfs(root)
        return self.res


sol = Solution()
tests = [
    ([4,2,1,3], [[1,2],[2,3],[3,4]]),
    ([1,3,6,10,15], [[1,3]]),
    ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.minimumAbsDifference(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
