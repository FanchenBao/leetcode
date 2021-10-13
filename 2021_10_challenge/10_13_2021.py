# from pudb import set_trace; set_trace()
from typing import List
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        """This one surprisingly is harder than I had expected. If I am
        currently at a node, and I am looking at preorder[idx]. If preorder[idx]
        is smaller than node.val, it is guaranteed that preorder[idx] is going
        to be the left child of node. Hence, that is our first check in the
        recursive function build().

        The tricky part is when preorder[idx] > node.val. It is possible that
        preorder[idx] is the right child of node, but it is also possible that
        it is the right child of node's ancestor. To evaluate this, we need to
        pass another value in build(), which is the min value that is bigger
        than node.val (min_big). In other words, we pass in the value of the smallest
        ancestor of node that is bigger than node. If preorder[idx] is smaller
        than this ancestor, we are certain that preorder[idx] is the current
        node's right child. Otherwise, we are done with the current branch and
        need to go back to our ancestor for further checking.

        Another tricky part is the root's min_big does not exist. Hence, we
        simply assign min_big the same as root.val. Thus, whenever preorder[idx]
        bubbles back to root, we know immediately that we need to go for the
        right branch.

        Finally, if we are on the left branch, the min_big is always the parent
        value. If we are on the right branch, the min_big is the same as the
        parent's min_big; or if the parent's min_big == parent.val, then the
        current node's min_big is the same as its value.

        O(N), 47 ms, 27% ranking.
        """
        root = TreeNode(val=preorder[0])
        n = len(preorder)
        self.idx = 1

        def build(node: TreeNode, min_big: int):
            if self.idx < n and node.val > preorder[self.idx]:
                node.left = TreeNode(val=preorder[self.idx])
                self.idx += 1
                build(node.left, node.val)
            if self.idx < n and node.val < preorder[self.idx]:
                if node.val < min_big < preorder[self.idx]:
                    return
                node.right = TreeNode(val=preorder[self.idx])
                self.idx += 1
                build(node.right, min_big if node.val != min_big else node.right.val)

        build(root, root.val)
        return root


class Solution2:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        """This is from DBabichev

        https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/discuss/1519096/Python-two-O(n)-solutions-explained

        This apparently is the correct answer, with binary search in mind.
        """
        n = len(preorder)
        self.idx = 0

        def build(lo: int, hi: int) -> TreeNode:
            if self.idx == n or not lo <= preorder[self.idx] <= hi:
                return None
            node = TreeNode(val=preorder[self.idx])
            self.idx += 1
            node.left = build(lo, node.val)
            node.right = build(node.val, hi)
            return node

        return build(-math.inf, math.inf)






        


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
