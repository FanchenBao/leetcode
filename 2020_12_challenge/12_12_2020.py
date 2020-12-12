# from pudb import set_trace; set_trace()
from typing import List, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        """Straightforward solution. First DFS to find paths for all leaf nodes
        (including leaf). Along the way we also track the max depth. The we
        filter the paths to retrieve those with the max depth. If only one
        path is remaining after the filter, we have a solo deepest node. We
        return that node immediately. If multiple paths exist after the filter,
        we compare all paths' ancestors from deep to shallow, one at a time.
        The first common ancestor we encounter is the deepest common ancestor.
        We return that one as answer.

        O(N + h) = O(N), 32 ms, 82% ranking.
        """
        paths = []
        max_depth = [0]

        def dfs(node: TreeNode, path: List):
            if not node.left and not node.right:  # leaf
                paths.append(path + [node])  # must include leaf in case leaf itself is the solo deepest node
                max_depth[0] = max(max_depth[0], len(path) + 1)
            else:
                path.append(node)
                if node.left:
                    dfs(node.left, path)
                if node.right:
                    dfs(node.right, path)
                path.pop()

        dfs(root, [])
        max_paths = [p[::-1] for p in paths if len(p) == max_depth[0]]
        if len(max_paths) == 1:  # only one deepest node, return leaf directly
            return max_paths[0][0]
        for ancestors in zip(*max_paths):  # find the first common ancestor
            for a1, a2 in zip(ancestors, ancestors[1:]):
                if a1.val != a2.val:
                    break
            else:
                return ancestors[0]



class Solution2:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        """Better solution using recursion. This comes from the official
        solution.

        The idea is at each node, we acquire the max depth of its left child
        and the deepest substree root on the left child, and we acquire the
        same on the right child.

        We then compare the max depth of both children, and take the deepest
        substree root of the deeper child as the return of the current node.

        If both children have the same depth, we return the current node
        directly.
        """

        def dfs(node: TreeNode) -> Tuple[TreeNode, int]:
            if not node:
                return None, 0
            L, R = dfs(node.left), dfs(node.right)
            return L[0], L[1] + 1 if L[1] > R[1] else R[0], R[1] + 1 if L[1] < R[1] else node, L[1] + 1

        return dfs(root)[0]


# sol = Solution3()
# tests = [
#     # ([1, 2, 3, 1], 3, 0, True),
#     # ([1, 0, 1, 1], 1, 2, True),
#     ([1, 5, 9, 1, 5, 9], 2, 3, False),
#     # ([1, 4, 9, 1, 4, 9], 1, 3, True),
#     # ([-1, -1], 1, -1, False),
#     # ([1, 3, 6, 2], 1, 2, True),
# ]

# for i, (nums, k, t, ans) in enumerate(tests):
#     res = sol.containsNearbyAlmostDuplicate(nums, k, t)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
