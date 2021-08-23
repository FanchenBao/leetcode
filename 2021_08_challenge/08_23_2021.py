# from pudb import set_trace; set_trace()
from typing import List, Optional
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """LeetCode 653

        We did not use BST at all. We simply turn the BST into a set, and use
        the regular method to solve Two Sums. I don't think using BST is going
        to make the solution any easier. The only benefit of using BST is to
        save memory usage.

        O(N) time, O(N) in space. 84 ms, 56% ranking.
        """
        vals = set()

        def dfs(node: Optional[TreeNode]) -> None:
            if node:
                vals.add(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        for v in vals:
            if k - v != v and k - v in vals:
                return True
        return False


class Solution1_1:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """Same as Solution1, but we can embed the checking in the dfs
        """
        vals = set()

        def dfs(node: Optional[TreeNode]) -> bool:
            if node:
                if k - node.val in vals:
                    return True
                vals.add(node.val)
                return dfs(node.left) or dfs(node.right)

        return dfs(root)


class Solution2:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """Trying to use BST and without extra space. O(NlogN)
        """
        min_val = math.inf
        node = root
        while node:
            min_val = min(min_val, node.val)
            node = node.left
        max_val = -math.inf
        node = root
        while node:
            max_val = max(max_val, node.val)
            node = node.right

        def search(node: Optional[TreeNode], target: int) -> bool:
            if node:
                if target == node.val:
                    return True
                elif target > node.val:
                    return search(node.right, target)
                else:
                    return search(node.left, target)
            return False

        def solve(node: Optional[TreeNode]) -> bool:
            if node:
                target = k - node.val
                if target > max_val:
                    return solve(node.right)
                if target < min_val:
                    return solve(node.left)
                if target != node.val and search(root, target):
                    return True
                return solve(node.left) or solve(node.right)
            return False

        return solve(root)


class Solution3:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """This is what the interviewer wants. BST iterators.

        Courtesy: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/discuss/1420711/C%2B%2BJavaPython-2-solutions%3A-HashSet-Iterators-Solutions-O(H)-space-Clean-and-Concise

        O(N) time, O(H) space, 72 ms
        """
        def push_left(node: Optional[TreeNode], node_list: List[TreeNode]) -> None:
            while node:
                node_list.append(node)
                node = node.left

        def push_right(node: Optional[TreeNode], node_list: List[TreeNode]) -> None:
            while node:
                node_list.append(node)
                node = node.right

        def next_left(node_list: List) -> int:
            node = node_list.pop()
            push_left(node.right, node_list)
            return node.val

        def next_right(node_list: List) -> int:
            node = node_list.pop()
            push_right(node.left, node_list)
            return node.val

        left_nodes, right_nodes = [], []
        push_left(root, left_nodes)
        push_right(root, right_nodes)
        # left and right are the values of the iterators going from both ends
        # of the BST towards the center
        left, right = next_left(left_nodes), next_right(right_nodes)
        while left < right:
            if left + right == k:
                return True
            elif left + right < k:
                left = next_left(left_nodes)
            else:
                right = next_right(right_nodes)
        return False


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
