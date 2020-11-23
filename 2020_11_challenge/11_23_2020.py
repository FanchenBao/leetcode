# from pudb import set_trace; set_trace()
from typing import List, Tuple
from collections import deque
import functools


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    @functools.lru_cache
    def rob(self, root: TreeNode, can_rob: bool = True) -> int:
        """Terrible runtime at 4872 ms. If without lru_cache, would TLE"""
        if not root:
            return 0
        if can_rob:
            gain1 = root.val + self.rob(root.left, False) + self.rob(root.right, False)
            gain2 = self.rob(root.left, True) + self.rob(root.right, True)
            return max(gain1, gain2)
        else:
            return self.rob(root.left, True) + self.rob(root.right, True)


class Solution2:
    @functools.lru_cache
    def helper(self, node: TreeNode) -> Tuple[int, int]:
        if not node:
            return 0, 0
        left_tup = self.helper(node.left)
        right_tup = self.helper(node.right)
        rob = node.val + left_tup[1] + right_tup[1]  # rob node
        not_rob = max(left_tup) + max(right_tup)
        return rob, not_rob

    def rob(self, root: TreeNode) -> int:
        """Follow the suggestion from the solution post to reduce the
        recursion call.

        52 ms, 42% ranking.
        """
        return max(self.helper(root))


def create_tree(nodes: List) -> TreeNode:
    """Build a binary tree based on the array input from LeetCode.
    
    :param nodes: The array of binary tree node values in the LeetCode format.
    :returns: The root node of the tree.
    """
    if not nodes:
        return None
    root = TreeNode(val=nodes[0])
    node_queue = deque()
    node_queue.append(root)
    i = 1
    while node_queue and i < len(nodes):
        curr = node_queue.popleft()
        curr.left = TreeNode(val=nodes[i]) if nodes[i] else None
        if i + 1 >= len(nodes):
            break
        curr.right = TreeNode(val=nodes[i + 1]) if nodes[i + 1] else None
        if curr.left:
            node_queue.append(curr.left)
        if curr.right:
            node_queue.append(curr.right)
        i += 2
    return root        


sol = Solution2()
tests = [
    ([3, 2, 3, None, 3, None, 1], 7),
    ([3, 4, 5, 1, 3, None, 1], 9),
    ([3, 1, None, 2, None, 4], 7),
    ([3], 3),
    ([], 0),
    ([2, 1, 3, None, 4], 7),
]

for i, (nodes, ans) in enumerate(tests):
    root = create_tree(nodes)
    res = sol.rob(root)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
