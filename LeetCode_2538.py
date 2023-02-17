# from pudb import set_trace; set_trace()
from typing import List, Tuple
import math
from collections import defaultdict


class Solution1:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        """Did not solve this. But I did see that the solution must be a path
        starting from a left but not ending in another leaf. The best way to
        think about this is from the post: https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/discuss/3052985/C%2B%2B-DFS

        The author correctly observed that this problem is almost identical in
        its core to 124. We can simply DFS this tree at any rooting (preferably
        at a rooting that is not a leaf). Then we can guarantee that the
        solution must be a path that goes from somewhere on the left subtree
        of a node, through the node, and end somewhere on the right subtree.
        Thus, if we can find the max path on the left, the max path on the right
        and we will have a candidate path rooted at the current node.

        We just need to go through this treating every single node as the
        current root node, and keep track of the max path sum at each node. The
        only differences between this problem and 124 are that

        1. this tree is not binary, but it is not difficult to overcome this
        small complexity.
        2. the path has to be with leaf on one subtree and without leaf on the
        other, which means for each node treated as root, we have to find two
        values. One is the max path starting from the root to the leaf
        containing the leaf. The other is the max path starting from the root
        but does not end in a leaf.
        3. All node values are positive, which actually makes this problem a bit
        easier.
        
        O(N), 2177 ms, faster than 74.69%
        """
        if n == 1:
            return 0
        if n == 2:
            return max(price)
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        root = 0  # pick root that is itself NOT a leaf
        while root < n and len(graph[root]) <= 1:
            root += 1
        self.res = 0

        def dfs(node: int, parent: int) -> Tuple[int, int]:
            """The return value is (max path with leaf, max path without leaf)"""
            max_leaf = max_no_leaf = 0
            for child in graph[node]:
                if child != parent:
                    sub_max_leaf, sub_max_no_leaf = dfs(child, node)
                    self.res = max(
                        self.res,
                        max_leaf + price[node] + sub_max_no_leaf,
                        max_no_leaf + price[node] + sub_max_leaf,
                    )
                    max_leaf = max(max_leaf, sub_max_leaf)
                    max_no_leaf = max(max_no_leaf, sub_max_no_leaf)
            return max_leaf + price[node], (max_no_leaf + price[node]) if len(graph[node]) > 1 else 0

        dfs(root, -1)
        return self.res


class Solution2:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        """Better implementation without having to consider edge case separately

        And because of that, root can be anything.
        """
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        self.res = 0

        def dfs(node: int, parent: int) -> Tuple[int, int]:
            """The return value is (max path with leaf, max path without leaf)"""
            # this considers the situation where node is a leaf
            max_leaf, max_no_leaf = price[node], 0
            for child in graph[node]:
                if child != parent:
                    sub_max_leaf, sub_max_no_leaf = dfs(child, node)
                    self.res = max(
                        self.res,
                        max_leaf + sub_max_no_leaf,
                        max_no_leaf + sub_max_leaf,
                    )
                    max_leaf = max(max_leaf, sub_max_leaf + price[node])
                    max_no_leaf = max(max_no_leaf, sub_max_no_leaf + price[node])
            return max_leaf, max_no_leaf

        dfs(0, -1)
        return self.res



sol = Solution2()
tests = [
    (6, [[0,1],[1,2],[1,3],[3,4],[3,5]], [9,8,7,6,10,5], 24),
    (3, [[0,1],[1,2]], [1,1,1], 2),
    (2, [[0,1]], [12,12], 12),
]

for i, (n, edges, price, ans) in enumerate(tests):
    res = sol.maxOutput(n, edges, price)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
