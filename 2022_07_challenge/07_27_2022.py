# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """LeetCode 114
        
        It's tricky. We traverse left to find the last node in a flattened left
        subtree. Here, if there is no left subtree, the last node on the left
        should be the current node.

        Then we traverse right to find the last node on a flattened right
        subtree. Very importantly, if there is no right subtree, the last node
        on the right should be the same as the last node on the left.

        Then we move the nodes around the current node, and we are done.

        O(N), 54 ms, faster than 60.12%
        """

        def helper(node: Optional[TreeNode]) -> TreeNode:
            if not node:
                return None
            last_left = helper(node.left) if node.left else node
            last_right = helper(node.right) if node.right else last_left
            last_left.right = node.right
            if node.left:
                node.right = node.left
                node.left = None
            return last_right

        helper(root)
        

class Solution2:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """This is the solution from a year ago using Morrison Traversal.

        The essence of Morrison Traversal is that we link the right child of
        the right most node of a left subtree to the right child of the root.
        This way, when we finish traversing the left subtree, we don't have to
        unwind the stack to go back to the root. Instead, we can simply call
        the right child of the right most node to go for the right child of the
        root.

        O(N)
        """
        node = root
        while node:
            head = node.left  # head of the left subtree
            if head:
                tail = head
                while tail.right:  # find the right most node
                    tail = tail.right
                tail.right = node.right  # Morrison link
                node.right = head
                node.left = None
            node = node.right

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
