# from pudb import set_trace; set_trace()
from typing import Dict, List
import math
from collections import defaultdict


class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        """
        Use binary lifting to create an anc matrix.
        """
        self.graph = defaultdict(list)
        for v, p in enumerate(parent):
            self.graph[p].append(v)
        self.MAX_DEPTH = (
            int(math.log2(n)) + 1
        )  # the upper bound of depth must be precise
        self.anc: Dict[int, list[int]] = defaultdict(lambda: [-1] * self.MAX_DEPTH)
        self.depth = [-1] * n
        self._build_ancestors(0, -1, 0)

    def _build_ancestors(self, node: int, par: int, depth: int) -> None:
        """
        Build an ancestor matrix such that anc[v][j] is the 2^j th ancestor of
        node v.
        """
        self.anc[node][0] = par
        self.depth[node] = depth
        j = 1
        while (1 << j) <= depth:
            self.anc[node][j] = self.anc[self.anc[node][j - 1]][j - 1]
            j += 1
        for child in self.graph[node]:
            self._build_ancestors(child, node, depth + 1)

    def getKthAncestor(self, node: int, k: int) -> int:
        """
        Break k into its binary representation, then we can use
        anc matrix to jump through each the ancestors using power
        of two.
        """
        j = 0
        p = node
        while k:
            if k & 1 != 0:
                p = self.anc[p][j]
            k >>= 1
            j += 1
        return p


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)


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
