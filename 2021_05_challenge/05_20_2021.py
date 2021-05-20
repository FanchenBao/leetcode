# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """LeetCode 102

        Simple BFS.

        O(N), 32 ms, 80% ranking.
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """DFS
        """
        res = []

        def dfs(node: TreeNode, lvl: int) -> None:
            if node:
                if len(res) == lvl:
                    res.append([])
                res[lvl].append(node.val)
                dfs(node.left, lvl + 1)
                dfs(node.right, lvl + 1)

        dfs(root, 0)
        return res


sol = Solution3()
tests = [
    ('abab', True),
    ('aba', False),
    ('abcabcabcabc', True),
    ('abcabcababcabcab', True),
    ('abcbac', False),
    ('aabaabaab', True),
    ('a', False),
    ('aaaaaaa', True),
    ('aaaaab', False),
]

for i, (s, ans) in enumerate(tests):
    res = sol.repeatedSubstringPattern(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
