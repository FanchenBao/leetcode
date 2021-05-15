# from pudb import set_trace; set_trace()
from typing import List, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def flatten(self, root: TreeNode) -> None:
        """LeetCode 114

        Do not return anything, modify root in-place instead.

        This is a recursion solution, so technically speaking it is not O(1).
        But we did make all the changes in-place. The idea is that given any
        root node, we want to process the left subtree, and return the head and
        tail of the linked list converted from the left subtree. Then we do the
        same on the right subtree. Then, we can construct the linked list based
        on the current tree by doing root.right = left_head, left_tail.right =
        right_head. And finally we return root and right_tail.

        The tricky part is handling nodes with no left or right child. Another
        tricky part is to not forget setting node.left to None. After these
        two tricky parts are resolved, the problem is solved.

        O(N), 36 ms, 74% ranking.
        """
        def helper(node: TreeNode) -> Tuple[TreeNode, TreeNode]:
            if node.left:
                next_head_l, next_tail_l = helper(node.left)
            else:
                next_head_l, next_tail_l = None, node
            if node.right:
                next_head_r, next_tail_r = helper(node.right)
            else:
                next_head_r, next_tail_r = None, None
            if next_head_l:
                node.right = next_head_l
            if next_head_r:
                next_tail_l.right = next_head_r
            node.left = None
            return node, next_tail_r if next_tail_r else next_tail_l
        
        if root:
            helper(root)


class Solution2:
    def flatten(self, root: TreeNode) -> None:
        """Morrison traversal from:

        https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/37010/Share-my-simple-NON-recursive-solution-O(1)-space-complexity!

        It is the same concept as Solution1, but done in an iterative fashion
        with a lot more ingenuity.

        O(N), because each node is visited twice. The right child is visited
        for the first time during the search for the right most node on the left
        subtree. It is visited again, when we call now = now.right to walk down
        the already flattened portion of the tree.

        The left child is visited for the first time in head = now.left. It is
        visited again after head is moved into the right place and
        now = now.right leads the current now to the head position.

        28 ms, 97% ranking.
        """
        now = root
        while now:
            head = now.left  # this is the head of the flattened left subtree
            if head:
                # the right most node on the left subtree is the tail of the
                # flattened left subtree
                tail = head
                while tail.right:
                    tail = tail.right
                tail.right = now.right
                now.right = head
                now.left = None
            now = now.right


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
