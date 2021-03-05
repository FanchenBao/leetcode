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
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        """BFS. Straightforward solution. Directly collect node values at each
        level and compute its average when a level has exhausted.

        O(N), 56 ms, 78% ranking.
        """
        if not root:
            return []
        queue = deque([(root, 0)])
        cur_lvl = 0
        res, temp = [], []
        while queue:
            node, lvl = queue.popleft()
            if lvl == cur_lvl:
                temp.append(node.val)
            else:
                res.append(sum(temp) / len(temp))
                temp = [node.val]
                cur_lvl = lvl
            if node.left:
                queue.append((node.left, lvl + 1))
            if node.right:
                queue.append((node.right, lvl + 1))
        res.append(sum(temp) / len(temp))
        return res


class Solution2:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        """DFS. Also pretty straightforward solution. When visiting each node,
        we add the node value to a list that tracks the sum of values on each
        lvl. We also increment a counter for total number of nodes on each lvl.
        Eventually, we can compute the average based on the lvl_sum and
        lvl_count arrays.

        O(N), 52 ms, 55% ranking.
        """
        lvl_sum, lvl_count = [], []

        def dfs(node: TreeNode, lvl: int) -> None:
            if node:
                if lvl == len(lvl_sum):
                    lvl_sum.append(0)
                    lvl_count.append(0)
                lvl_sum[lvl] += node.val
                lvl_count[lvl] += 1
                dfs(node.left, lvl + 1)
                dfs(node.right, lvl + 1)

        dfs(root, 0)
        return [s / c for s, c in zip(lvl_sum, lvl_count)]


class Solution3:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        """BFS version of the DFS.

        O(N), 56 ms, 32% ranking.
        """
        queue = deque([(root, 0)])
        res = []
        cur_lvl, s, c = 0, 0, 0
        while queue:
            node, lvl = queue.popleft()
            if node:
                if lvl != cur_lvl:
                    res.apend(s / c)
                    s, c = 0, 0
                    cur_lvl
                s += node.val
                c += 1
                queue.append((node.left, lvl + 1))
                queue.append((node.right, lvl + 1))
        return res


class Solution4:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        """A better BFS without the need of using lvl to keep track of levels.
        I think this is the official way to do BFS. Two queues, one trakcing the
        current level and another the next level. When the current level is
        exhausted, we replace the current level with the next level. This way,
        we avoid the need of manually checking whether a level has exhausted
        using the "lvl" variable.

        O(N), 48 ms, 78% ranking.
        """
        queue = deque([root])
        res = []
        while queue:
            next_lvl = deque()
            s, c = 0, 0
            while queue:
                node = queue.popleft()
                if not node:
                    continue
                s += node.val
                c += 1
                next_lvl.append(node.left)
                next_lvl.append(node.right)
            if c != 0:
                res.append(s / c)
            queue = next_lvl
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
