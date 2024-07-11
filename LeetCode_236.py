# from pudb import set_trace; set_trace()
from collections import defaultdict
from typing import Dict, List, Optional
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kth_ancestor(self, node: int, k: int, anc: Dict[int, List[int]]) -> int:
        idx = 0
        res = node
        while k:
            if k & 1 == 1:
                res = anc[res][idx]
            k >>= 1
            idx += 1
        return res

    def create_anc_matrix(
        self,
        node: Optional[TreeNode],
        parent: TreeNode,
        dep: int,
        depths: Dict[int, int],
        anc: Dict[int, List[int]],
    ) -> None:
        if node is None:
            return
        depths[node.val] = dep
        anc[node.val].append(parent.val)
        i = 1
        while (1 << i) <= dep:
            anc[node.val].append(anc[anc[node.val][i - 1]][i - 1])
            i += 1
        self.create_anc_matrix(node.left, node, dep + 1, depths, anc)
        self.create_anc_matrix(node.right, node, dep + 1, depths, anc)

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """
        Practice binary lifting to solve this problem
        """
        anc: Dict[int, List[int]] = defaultdict(list)
        depths: Dict[int, int] = {}
        self.create_anc_matrix(root, root, 0, depths, anc)
        pv = p.val
        qv = q.val
        if depths[pv] > depths[qv]:
            pv, qv = qv, pv
        qv = self.kth_ancestor(qv, depths[qv] - depths[pv], anc)
        if pv == qv:
            return TreeNode(pv)
        for lvl in range(depths[pv], -1, -1):
            ap = self.kth_ancestor(pv, lvl, anc)
            aq = self.kth_ancestor(qv, lvl, anc)
            if ap != aq:
                pv, qv = ap, aq
        return TreeNode(anc[pv][0])


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
