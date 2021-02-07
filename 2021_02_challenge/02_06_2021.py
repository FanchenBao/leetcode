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
    def rightSideView(self, root: TreeNode) -> List[int]:
        """I initially wanted to use DFS, and only going down on the right
        branch. This strategy looked promising at the beginning, but I failed a
        test case, where the bottom level only has one node and it is on the
        left branch. Thus, DFS going down the right branch is not going to work.

        However, we can use BFS, to traverse the tree. The only thing we need
        to take care of is to identify when the last node on a level is
        encountered. The current solution use a pre_node and pre_lvl to record
        the previous node encountered. This way, when the current node's lvl is
        different from pre_lvl, we know that pre_node is the last node on
        pre_lvl. We just need to push the pre_node's value to a result list.

        O(N), 40 ms, 19% ranking.
        """
        res = []
        if not root:
            return res
        queue = deque([(root, 0)])  # (node, lvl)
        pre_node, pre_lvl = None, -1

        while queue:
            node, lvl = queue.popleft()
            if node.left:
                queue.append((node.left, lvl + 1))
            if node.right:
                queue.append((node.right, lvl + 1))
            if lvl != pre_lvl and pre_node:
                res.append(pre_node.val)
            pre_node, pre_lvl = node, lvl

        res.append(pre_node.val)
        return res


class Solution2:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """A brilliant recursion solution. I thought DFS is not going to work.
        It won't work the way I was thinking about it, but this method, supplied
        by https://leetcode.com/problems/binary-tree-right-side-view/discuss/56003/My-C%2B%2B-solution-modified-preorder-traversal
        works perfectly. The key insight is that the length of the result list
        is the same as the depth of the tree, and at each level of the tree,
        only one value can be pushed to the result list. Therefore, we can
        compare the size of the result list and the current level of a node to
        determine whether the current node should be pushed into the list. If
        the current node, which is always right branch first, has level larger
        than the size of the current list, that means the current node is on
        a new level. Thus, its value should be pushed to the result list. When
        the traversal hits the left branch, the comparison between the level and
        size of the result list also helps to identify any left child that is
        on a level not reached by the result list.

        O(N), 32 ms, 71% ranking.
        """
        res = []

        def dfs(node: TreeNode, lvl: int):
            if node:
                if lvl > len(res):
                    res.append(node.val)
                dfs(node.right, lvl + 1)
                dfs(node.left, lvl + 1)

        dfs(root, 1)
        return res


class Solution3:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """El mejor BFS (sort of), proveido por Mr. Pochmann:
        https://leetcode.com/problems/binary-tree-right-side-view/discuss/56064/5-9-Lines-Python-48%2B-ms

        Its sort of a BFS, but it basically expands each level of the tree, and
        take the last value of each level. Very straightforward, but works
        pretty well.

        Also notice the nested list comprehension ordering. The top level "for"
        comes first.

        O(N), 32 ms, 71% ranking.
        """
        if not root:
            return []
        res = []
        level = [root]
        while level:
            res.append(level[-1].val)
            level = [child for node in level for child in (node.left, node.right) if child]
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
