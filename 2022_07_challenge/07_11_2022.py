# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """LeetCode 199

        Straightforward BFS

        O(N), 50 ms, faster than 51.41% 
        """
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            temp = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            res.append(node.val)
        return res


class Solution2:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """DFS

        O(N), 38 ms, faster than 83.60% 
        """
        res = []

        def dfs(node: Optional[TreeNode], lvl: int) -> None:
            if node:
                if len(res) == lvl:
                    res.append(node.val)
                else:
                    res[lvl] = node.val
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
