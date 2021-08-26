# from pudb import set_trace; set_trace()
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class Solution1:
    def isValidSerialization(self, preorder: str) -> bool:
        """LeetCode 331

        This one works because we reconstructed the tree. However, it is not
        following the requirement, so we won't count this.

        O(N) time and O(N) space, 64 ms, 5% ranking.
        """
        self.idx = 0
        self.valid = True
        preorder_lst = preorder.split(',')

        def construct() -> Optional[TreeNode]:
            if self.idx == len(preorder_lst):
                self.valid = False
                return None
            val = preorder_lst[self.idx]
            self.idx += 1
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = construct()
            node.right = construct()
            return node

        construct()
        return self.valid and self.idx == len(preorder_lst)


class Solution2:
    def isValidSerialization(self, preorder: str) -> bool:
        """The same logic as Solution1 but without constructing the tree
        explicitly.

        O(N) time, O(N) space, 36 ms, 54% ranking.
        """
        rev_lst = preorder.split(',')[::-1]

        def construct() -> bool:
            if not rev_lst:
                return False
            val = rev_lst.pop()
            if val == '#':
                return True
            if not construct() or not construct():
                return False
            return True

        return construct() and not rev_lst


class Solution3:
    def isValidSerialization(self, preorder: str) -> bool:
        """Very very smart idea from:

        https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/discuss/1426956/Python3Java-Easy-Solution-Explained-in-Detail-or-O(1)-Space

        Using a slot concept. Each non-null node takes one slot and offers two
        additional slots. So the net slot for non-null node is 1. Each null
        node takes one slot and offers zero slot. So the net slot for null node
        is -1. For preorder to be valid, as we iterate through each node, the
        net slot must not be negative and at the end the net slot must be zero.
        """
        preorder_lst = preorder.split(',')
        slot = 1  # initial slot is one because we need to hold the root
        for val in preorder_lst:
            if slot == 0:
                return False
            slot += -1 if val == '#' else 1
        return slot == 0


sol = Solution3()
tests = [
    ('9,3,4,#,#,1,#,#,2,#,6,#,#', True),
    ('1,#', False),
    ('9,#,#,1', False),
    ('#', True),
    ('#,#,3,5,#', False),
    ('#,7,6,9,#,#,#', False),
]

for i, (preorder, ans) in enumerate(tests):
    res = sol.isValidSerialization(preorder)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
