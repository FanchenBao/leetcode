# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.

        LeetCode 99

        This is much harder than I had expected. The O(n) space solution is not
        difficult, but O(1) space requires some ingenuity. My solution here
        comes from the observation that in a sorted list of numbers, if one
        pair gets swapped, we can identify the left member of the swapped pair
        by going left to right on the sorted list. The first number that is
        out of position is the left member of the swapped pair. Similarly, we
        can go right to left on the sorted list, and the first number that is
        out of position is the right member of the swapped pair. Then we simply
        swapped those two members and we are done.

        O(N) time and O(1) space. 100 ms, 49.52%
        """
        self.err_node1 = None
        self.err_node2 = None

        def inorder(node: Optional[TreeNode]) -> bool:
            if node:
                if inorder(node.left):
                    return True
                if self.err_node1 and self.err_node1.val > node.val:
                    return True
                self.err_node1 = node
                return inorder(node.right)
            return False

        def postorder(node: Optional[TreeNode]) -> bool:
            if node:
                if postorder(node.right):
                    return True
                if self.err_node2 and self.err_node2.val < node.val:
                    return True
                self.err_node2 = node
                return postorder(node.left)
            return False

        inorder(root)
        postorder(root)
        self.err_node1.val, self.err_node2.val = self.err_node2.val, self.err_node1.val


class Solution2:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """A better O(1) space solution. I coded this up on 2020-11-01.

        The basic idea is the same as Solution1, but instead of two traversals,
        we only need to do one and record the four nodes that are involved in
        mismatching. Since each mismatch is caught by self.pre.val > node.val,
        the list of four nodes will have this pattern [big, small, big, small].
        It is guaranteed that the first big and the last small are the wrong
        nodes. So we just need to swap those two.
        """
        self.pre = None
        nodes = []

        def inorder(node: Optional[TreeNode]) -> bool:
            if node:
                inorder(node.left)
                if self.pre and self.pre.val > node.val:
                    nodes.extend([self.pre, node])
                self.pre = node
                inorder(node.right)

        inorder(root)
        nodes[0].val, nodes[-1].val = nodes[-1].val, nodes[0].val



# sol = Solution()
# tests = [
#     ([4,2,1,3], [[1,2],[2,3],[3,4]]),
#     ([1,3,6,10,15], [[1,3]]),
#     ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
# ]

# for i, (arr, ans) in enumerate(tests):
#     res = sol.minimumAbsDifference(arr)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
