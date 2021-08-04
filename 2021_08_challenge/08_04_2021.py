# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        """LeetCode 113

        A typical DFS with backtracking solution. Nothing too fancy. The only
        trick that I need is to deliberately check for a leaf node. If I don't
        do that and check whether a node is None as the base case for recursion,
        we will duplicate each path, because we visit the left and right
        children of a leaf. If this leaf is indeed the last node in a path, we
        would have append the same path twice.

        O(N), 48 ms, 50% ranking.

        UPDATE: regarding time complexity, I forgot to consider the copy when
        a solution is found. The copy will take O(logN) if the tree is balanced,
        but O(N) otherwise. Therefore, the worst case scenario time complexity
        is O(N^2).
        """
        res = []

        def dfs(node: TreeNode, cur_sum: int, cur_path: List[int]) -> None:
            cur_path.append(node.val)
            cur_sum += node.val
            if node.left is None and node.right is None:  # check for leaf
                if cur_sum == targetSum:
                    res.append(cur_path[:])
            else:
                if node.left:
                    dfs(node.left, cur_sum, cur_path)
                if node.right:
                    dfs(node.right, cur_sum, cur_path)
            # Backtracking
            cur_path.pop()
            cur_sum -= node.val

        if root:  # handle edge case of empty tree
            dfs(root, 0, [])
        return res


class Solution2:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        """BFS"""
        if not root:
            return []
        queue = [(root, 0, [])]
        res = []
        while queue:
            temp = []
            for node, cur_sum, cur_path in queue:
                cur_sum += node.val
                cur_path.append(node.val)
                if not node.left and not node.right and cur_sum == targetSum:
                    res.append(cur_path)
                else:
                    if node.left:
                        temp.append((node.left, cur_sum, cur_path[:]))
                    if node.right:
                        temp.append((node.right, cur_sum, cur_path[:]))
            queue = temp
        return res


# sol = Solution3()
# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
