# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """LeetCode 863

        Turn the tree into a graph and then BFS.

        O(N), 58 ms, faster than 35.25%
        """
        graph = defaultdict(list)

        def dfs(node: TreeNode) -> None:
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                dfs(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                dfs(node.right)

        dfs(root)
        queue = [target.val]
        visited = set([target.val])
        while queue and k:
            tmp = []
            for node in queue:
                for child in graph[node]:
                    if child not in visited:
                        visited.add(child)
                        tmp.append(child)
            queue = tmp
            k -= 1
        return queue


# sol = Solution()
# tests = [
#     ([3,5,1,6,2,0,8,null,null,7,4], 5, 2, [7,4,1]),
#     ([1], 1, 3, []),
# ]

# for i, (root, target, ans) in enumerate(tests):
#     res = sol.distanceK(root, target, k)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
