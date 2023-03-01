# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution1:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        """LeetCode 652

        DFS and hash each subtree. The way of hashing is to turn each value into
        string and concatenate all the strings with the following rules:

        left hash + ( + root.val + ) + right hash

        Initially, I didn't use the left and right parentheses to indicate the
        left and right children. And that led to a failed test case. Thus, to
        differentiate the left and right children, I put two distinct char when
        connecting the left and right children.

        O(N * N), 55 ms, faster than 64.17%
        """
        m = defaultdict(list)

        def dfs(node: Optional[TreeNode]) -> str:
            if node:
                hash_left = dfs(node.left)
                if not hash_left:
                    hash_left = '('
                hash_right = dfs(node.right)
                if not hash_right:
                    hash_right = ')'
                h = hash_left + '(' + str(node.val) + ')' + hash_right
                m[h].append(node)
                return h
            return ''

        dfs(root)
        return [v[0] for v in m.values() if len(v) >= 2]


class Solution2:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        """This is inspired by the triplet ID method in the official solution.

        We assign an ID to all subtrees. If two subtrees have the same ID, they
        must be duplicate. To generate the ID, we use a triplet to represent
        each subtree. The subtree triplet is

        (left ID, root.val, right ID)

        If this triplet has been seen before, we return the ID associated with
        this triplet as the ID of the curretn subtree. Otherwise, we create a
        new unique ID for the current triplet. One way to create such ID is to
        take the length of the triplet_to_id dict and plus 1.

        This is super smart.

        O(N), 49 ms, faster than 85.04% 
        """
        m = defaultdict(list)
        triplet_to_id = {}

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            trip = (dfs(node.left), node.val, dfs(node.right))
            if trip not in triplet_to_id:
                triplet_to_id[trip] = len(triplet_to_id) + 1
            trip_id = triplet_to_id[trip]
            m[trip_id].append(node)
            return trip_id

        dfs(root)
        return [v[0] for v in m.values() if len(v) >= 2]





# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
