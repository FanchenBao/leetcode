# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        """Given the two nodes in queries, we need to find their most recent
        common ancestor. The cycle size is the height from the most recent
        common ancestor to one node plus the height from the most recent common
        ancestor to the other node plus one.

        Since we are given a complete binary tree, we can divide each node by 2
        to find all the nodes on its path. Thus, finding two node's most recent
        common ancestor is equivalent to find the largest node shared
        in their paths. We can achieve that by using set to represent the path
        and find the max of the intersection of the set.
        
        The height of a node can be computed as math.floor(math.log2(node))

        O(MlogN), 3182 ms, faster than 51.94%
        """
        dp = {}

        def common_ancestor(a: int, b: int) -> int:
            if a not in dp:
                dp[a] = set()
                tmp = a
                while tmp > 0:
                    dp[a].add(tmp)
                    tmp //= 2
            if b not in dp:
                dp[b] = set()
                tmp = b
                while tmp > 0:
                    dp[b].add(tmp)
                    tmp //= 2
            return max(dp[a].intersection(dp[b]))

        res = []
        for a, b in queries:
            ca = common_ancestor(a, b)
            ha, hb, hca = math.floor(math.log2(a)), math.floor(math.log2(b)), math.floor(math.log2(ca))
            res.append(ha - hca + hb - hca + 1)
            self.ca = 0
        return res


class Solution2:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        """lee215's method of finding Lowest Common Ancestor of two nodes in a
        complete binary tree. Brilliant!

        O(MlogN), 3316 ms, faster than 49.03%
        """
        res = []
        for a, b in queries:
            res.append(1)
            while a != b:
                # this is brilliant. Each time, we keep the smaller of the two
                # nodes and get the parent of the larger node. Notice that by
                # doing this, if the two nodes are on the same level, it is
                # guaranteed that one will get elevated earlier than the other,
                # which means the one that goes up earlier always waits for the
                # other one.
                a, b = min(a, b), max(a, b) // 2
                res[-1] += 1
        return res


sol = Solution2()
tests = [
    (3, [[5,3],[4,7],[2,3]], [4,5,3]),
    (2, [[1,2]], [2]),
]

for i, (n, queries, ans) in enumerate(tests):
    res = sol.cycleLengthQueries(n, queries)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
