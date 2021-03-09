# from pudb import set_trace; set_trace()
from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        """Fairly easy. We use dfs to find the node of interest, which is the
        node at d - 1 depth. From there, we can create new node and attach the
        original left and right subtree root to the left and right branch of
        the new nodes. We also have to set up a special case for d = 1.

        O(N), 52 ms, 82% ranking.
        """
        if d == 1:
            return TreeNode(val=v, left=root)

        def dfs(node: TreeNode, lvl: int) -> None:
            if node:
                if lvl == d - 1:
                    node.left = TreeNode(val=v, left=node.left)
                    node.right = TreeNode(val=v, right=node.right)
                elif lvl < d - 1:
                    dfs(node.left, lvl + 1)
                    dfs(node.right, lvl + 1)

        dfs(root, 1)
        return root


class Solution2:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        """BFS. Plus I think this is actually the best way to do BFS, with one
        queue and efficient in memory. Notice that we use len(queue) to
        determine how many nodes are in a level. This way, we can keep pushing
        new nodes into the queue while still being able to stop once a level is
        completely traversed.

        O(N), 52 ms, 82% ranking.
        """
        if d == 1:
            return TreeNode(val=v, left=root)

        queue = deque([root])
        lvl = 1
        while lvl < d - 1:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            lvl += 1
        while queue:
            node = queue.popleft()
            node.left = TreeNode(val=v, left=node.left)
            node.right = TreeNode(val=v, right=node.right)
        return root


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
