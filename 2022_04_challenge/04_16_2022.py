# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """LeetCode 538

        This is a modified problem to find the sum of the entire tree. For each
        node, its val must add to the sum of the right subtree. And it must
        also add its parent's val if it is the left branch of its parent. Based
        this, we can use the algorithm to find sum of a tree, but add a parent
        val when passing to the subtree. When calling the right subtree from
        the root, the parent val is set to 0. Otherwise, the parent val is
        either the current node's val if passing to the left subtree, or some
        parent val inherited from previous recursions.

        O(N), 75 ms, 98.41%
        """

        def helper(node: Optional[TreeNode], pval: int) -> int:
            if not node:
                return 0
            rsum = helper(node.right, pval)
            # node's val must include the right subtree sum and its parent val
            # if exists
            node.val += rsum + pval
            # When going to the left subtree, we supply the updated node's val
            # because it has recorded the sum of all nodes that are larger than
            # all the node in the left subtree.
            lsum = helper(node.left, node.val)
            return node.val + lsum - pval  # return just the sum of the subtree

        helper(root, 0)
        return root


class Solution2:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """This is the official solution. Going right -> root -> left is
        naturally the reverse order of all values. So we just keep track of the
        total and we have the value to add to each node.
        """
        self.total = 0

        def helper(node: Optional[TreeNode]) -> None:
            if node:
                helper(node.right)
                self.total += node.val
                node.val = self.total
                helper(node.left)

        helper(node)
        return root


        

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
