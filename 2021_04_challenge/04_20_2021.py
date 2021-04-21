# from pudb import set_trace; set_trace()
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution1:
    def preorder(self, root: Node) -> List[int]:
        """LeetCode 589

        Trivial recursion solution

        O(N), 52 ms, 57% ranking.
        """

        def dfs(node: Node) -> None:
            if node:
                res.append(node.val)
                for child in node.children:
                    dfs(child)

        res = []
        dfs(root)
        return res


class Solution2:
    def preorder(self, root: Node) -> List[int]:
        """Iterative version. A bit more complicated than the recursion, but
        the concept is exactly the same. The trick is when a node is pushed to
        the stack, we also have to push the index of the current child to be
        visited. And as a node's children are visited, this index increments to
        move to the next child.

        O(N), 56 ms.
        """
        stack = [(root, 0)]
        res = []
        while stack:
            node, idx = stack.pop()
            if node:
                if idx == 0:
                    res.append(node.val)
                if idx < len(node.children):
                    stack.extend(
                        [(node, idx + 1), (node.children[idx], 0)],
                    )
        return res


class Solution3:
    def preorder(self, root: Node) -> List[int]:
        """This is the official iterative solution.
        The difference between this iterative solution and mine is that it does
        not have to keep the parent in the stack. The trick is to add all the
        children to the stack in reverse order. This way, the most left child
        will always get popped first.
        """
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                for child in node.children[::-1]:
                    stack.append(child)
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
