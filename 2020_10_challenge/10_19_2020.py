# from pudb import set_trace; set_trace()
from typing import Dict


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:

    def visit(self, node: Node, node_catalog: Dict):
        node_clone = Node(node.val)
        node_catalog[node.val] = node_clone
        for next_node in node.neighbors:
            if next_node.val not in node_catalog:
                self.visit(next_node, node_catalog)
            node_clone.neighbors.append(node_catalog[next_node.val])

    def cloneGraph(self, node: Node) -> Node:
        """58% ranking. DFS approach"""
        node_catalog = {}
        if not node:
            return None
        self.visit(node, node_catalog)
        return node_catalog[node.val]
