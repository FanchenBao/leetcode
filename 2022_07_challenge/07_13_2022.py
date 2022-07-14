# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """LeetCode 102

        O(N), 59 ms, faster than 37.38%
        """
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            temp = []
            res.append([])
            for node in queue:
                res[-1].append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
        return res


class Solution2:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """DFS

        38 ms, faster than 88.88%
        """
        res = []

        def dfs(node: Optional[TreeNode], lvl: int) -> None:
            if node:
                if len(res) == lvl:
                    res.append([])
                res[lvl].append(node.val)
                dfs(node.left, lvl + 1)
                dfs(node.right, lvl + 1)

        dfs(root, 0)
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
