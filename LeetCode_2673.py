# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        """Maybe we can count this as greedy? The idea is to equate the cost
        sum of the two subtrees for all levels. And the difference of the
        current cost sum of the two subtrees is the additional steps we must
        take.

        O(N), 1399 ms, faster than 74.35% 
        """
        self.res = 0

        def solve(node: int) -> int:
            if 2 * node > n:  # node is a leaf
                return cost[node - 1]
            lc, rc = solve(2 * node), solve(2 * node + 1)
            self.res += abs(lc - rc)
            return cost[node - 1] + max(lc, rc)

        solve(1)
        return self.res


sol = Solution()
tests = [
    (7, [1,5,2,2,3,3,1], 6),
    (3, [5,3,3], 0),
]

for i, (n, cost, ans) in enumerate(tests):
    res = sol.minIncrements(n, cost)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
