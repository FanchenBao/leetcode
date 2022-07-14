# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """LeetCode 105

        We use preorder as the order of progression. Use inorder as the
        recursion structure. Preorder visits the root. Then we can find in
        inorder the location of the root and divide inorder into two halves.
        We continue with preorder and visit the left half of inorder. Whenever
        the current node of preorder lands in a value that is outside the
        current range of inorder, that means we have finished all the nodes
        on that side. We need to switch to the right side.

        The only tricky part is to keep track of the current progression on
        preorder. We use the return value of recursion to do that for us.

        O(N), 76 ms, faster than 90.33%
        """
        nodes_dict = {v: (i, TreeNode(val=v)) for i, v in enumerate(inorder)}
        N = len(preorder)

        def build(lo: int, hi: int, pi: int) -> Tuple[Optional[TreeNode], int]:
            if pi >= N:
                return None, pi - 1
            ii, node = nodes_dict[preorder[pi]]
            if lo <= ii <= hi:
                node.left, npi = build(lo, ii - 1, pi + 1)
                node.right, npi = build(ii + 1, hi, npi + 1)
                return node, npi
            return None, pi - 1

        return build(0, N - 1, 0)[0]


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
