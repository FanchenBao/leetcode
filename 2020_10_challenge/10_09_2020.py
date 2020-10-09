# from pudb import set_trace; set_trace()
from typing import List, Deque
import json
from collections import deque
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec1:
    """35% ranking. Apparently cheated by using JSON."""

    def traverse_tree(self, node: TreeNode, serialized: List[int]) -> None:
        if node:
            serialized.append(node.val)
            self.traverse_tree(node.left, serialized)
            self.traverse_tree(node.right, serialized)

    def insert_node(self, node: TreeNode, val: int) -> TreeNode:
        if not node:
            return TreeNode(val)
        if node.val > val:
            node.left = self.insert_node(node.left, val)
        else:
            node.right = self.insert_node(node.right, val)
        return node

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        serialized = []
        self.traverse_tree(root, serialized)
        return json.dumps(serialized)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        root = None
        for val in json.loads(data):
            root = self.insert_node(root, val)
        return root


class Codec2:
    """NOT using JSON library
    
    And after reading the discussion, I just realized why my solution was slow:
    it was O(nlog(n)). I insert a node from the root each time. The best
    solution has time complexity O(n), which means it builds the tree as it
    traverses down the tree. See Codec3 for the O(n) solution.
    """

    def traverse_tree(self, node: TreeNode, serialized: List[int]) -> None:
        if node:
            serialized.append(str(node.val))
            self.traverse_tree(node.left, serialized)
            self.traverse_tree(node.right, serialized)

    def insert_node(self, node: TreeNode, val: int) -> TreeNode:
        if not node:
            return TreeNode(val)
        if node.val > val:
            node.left = self.insert_node(node.left, val)
        else:
            node.right = self.insert_node(node.right, val)
        return node

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        serialized = []
        self.traverse_tree(root, serialized)
        return ','.join(serialized)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        root = None
        if data:
            for val in data.split(','):
                root = self.insert_node(root, int(val))
        return root


class Codec3:
    """O(N) solution. 90% ranking."""

    def traverse_tree(self, node: TreeNode, serialized: List[int]) -> None:
        if node:
            serialized.append(str(node.val))
            self.traverse_tree(node.left, serialized)
            self.traverse_tree(node.right, serialized)

    def build_tree(self, deserialized: Deque[int], min_val, max_val) -> TreeNode:
        # the min_val < deserialized[0] < max_val is crucial for rebuilding
        # the binary tree. This statement makes sure that the next value is
        # suitable to be built at the current tree location.
        if deserialized and min_val < deserialized[0] < max_val:
            node = TreeNode(deserialized.popleft())
            node.left = self.build_tree(deserialized, min_val, node.val)
            node.right = self.build_tree(deserialized, node.val, max_val)
            return node
        return None

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        serialized = []
        self.traverse_tree(root, serialized)
        return ','.join(serialized)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        deserialized = deque(data.split(','))
        return self.build_tree(deserialized, -math.inf, math.inf)




# sol = Solution3()
# tests = [
#     # ([1, 2, 3, 1], 3, 0, True),
#     # ([1, 0, 1, 1], 1, 2, True),
#     ([1, 5, 9, 1, 5, 9], 2, 3, False),
#     # ([1, 4, 9, 1, 4, 9], 1, 3, True),
#     # ([-1, -1], 1, -1, False),
#     # ([1, 3, 6, 2], 1, 2, True),
# ]

# for i, (nums, k, t, ans) in enumerate(tests):
#     res = sol.containsNearbyAlmostDuplicate(nums, k, t)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
