# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """LeetCode 222

        This solution runs in O(N) in worst case scenario, but O(logN) in
        best case. Worst case is that the last level has one fewer node to make
        the tree a perfect binary tree. The best case is a perfect binary tree.

        The idea is to first go all the way down on the right branch. This tells
        us the height of the tree h, probably minus the last level. Then we
        perform the regular dfs, stopping at height h. Then we probe to count
        the total number of leaves. We stop when we encounter the node that only
        has one leaf. Thus, the farther right the single-child node is located,
        the closer the complexity goes from O(logN) towards O(N).

        84 ms, 65% ranking.
        """
        if not root:
            return 0
        h = 0
        node = root
        while node.right:
            node = node.right
            h += 1
        self.num_leaf = 0

        def dfs(node: TreeNode, lvl: int) -> bool:
            if lvl < h:
                if dfs(node.left, lvl + 1) or dfs(node.right, lvl + 1):
                    return True
                return False
            elif lvl == h:
                if node.left:
                    self.num_leaf += 1
                if node.right:
                    self.num_leaf += 1
                    return False
                return True

        dfs(root, 0)
        return 2**(h + 1) - 1 + self.num_leaf



class Solution2:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """Pure dfs
        """
        if not root:
            return 0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1


class Solution3:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """Pure bfs
        """
        if not root:
            return 0
        queue = [root]
        res = 0
        while queue:
            res += len(queue)
            temp = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
        return res


class Solution4:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """This one is slower. Probably O(NlogN)
        """
        if not root:
            return 0
        node = root
        hl, hr = 0, 0
        while node.left:
            node = node.left
            hl += 1
        while node.right:
            node = node.right
            hr += 1
        if hl == hr:
            return 2**(hl + 1) - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """This is the real deal, from Mr. Pochmann himself.

        https://leetcode.com/problems/count-complete-tree-nodes/discuss/61958/Concise-Java-solutions-O(log(n)2)

        We compute the hight of the tree at each node. But this is the real
        height, which means we always go down the left branch. If the heights
        of the left subtree and the right subtree are the same, that means the
        left subtree is perfect. So we don't have to worry about the left
        subtree anymore and recurse on the right instead. Similarly, if the
        height of the right subtree is one fewer than the left subtree, that
        means the right subtree is perfect, and we only need to recurse on the
        left instead.

        O((logN)^2)
        """

        def height(node: TreeNode) -> int:
            """Note that we designate -1 as the height of an empty tree. Because
            the formula to compute the total number of nodes in a perfect tree
            stipulates that when height is -1, the number of nodes is 0. It's
            very fitting for our use case.
            """
            h = -1
            while node:
                node = node.left
                h += 1
            return h

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            hl = height(node.left)
            hr = height(node.right)
            if hl == hr:
                return 2**(hl + 1) - 1 + dfs(node.right) + 1
            return 2**(hr + 1) - 1 + dfs(node.left) + 1

        return dfs(root)




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
