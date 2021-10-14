# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache
import math
from bisect import bisect_right


class Solution1:
    def numSquares(self, n: int) -> int:
        """LeetCode 279

        The initial attempt TLE, which I think was due to the use of too much
        sqrt operation. Thus, in this version, we precompute all the possible
        perfect square condidates, and then use binary search to determine the
        largest perfect square each subsequent target can use.

        Then comes the key trick: we can stop searching early if we can be sure
        that the result we have found so far is already the best we can get. To
        evaluate this, we always check the perfect squares from large to small.
        For each large perfect square, we can obtain a result. Then for the next
        large perfect square, we can multiply it with the result obtained
        previously. If the product is smaller than our target, that means even
        if using only this large perfect square, we cannot reach our target.
        Thus, any further search is futile, and we can terminate right there.

        With this trick and the use of binary search, we obtain runtime at
        538 ms, 74% ranking.

        NOTE: Time complexity is O(n * sqrt(n)), I got it wrong again.
        """
        squares = [sqrt**2 for sqrt in range(1, int(math.sqrt(n)) + 1)]

        @lru_cache(maxsize=None)
        def solve(target: int) -> int:
            idx = bisect_right(squares, target)
            if squares[idx - 1] == target:
                return 1
            if squares[idx - 1] == 1:
                return target
            res = math.inf
            for i in range(idx - 1, -1, -1):
                if res * squares[i] < target:
                    break
                res = min(res, solve(target - squares[i]) + 1)
            return res

        return solve(n)


class Solution2:
    def numSquares(self, n: int) -> int:
        """Same as solution1, but with greedy, i.e. each time we only take as
        many largest perfect square that we can take as possible at the moment.
        This works because if we can take a large perfect square, it is always
        better to take that instead of takeing multiple smaller perfect squares.

        This one is a lot faster. 160 ms, 92% ranking. Greedy is the way to go.
        """
        squares = [sqrt**2 for sqrt in range(1, int(math.sqrt(n)) + 1)]

        @lru_cache(maxsize=None)
        def solve(target: int) -> int:
            if not target:
                return 0
            idx = bisect_right(squares, target)
            res = math.inf
            for i in range(idx - 1, -1, -1):
                if res * squares[i] < target:
                    break
                q, r = divmod(target, squares[i])
                res = min(res, solve(r) + q)
            return res

        return solve(n)


class Solution3:
    def numSquares(self, n: int) -> int:
        """Bottom up DP. Courtesty:

        https://leetcode.com/problems/perfect-squares/discuss/1520447/c%2B%2B-dp-easy-to-understand

        Very nice explanation there. However, this method is slower than
        Solution2, because with bottom up, we have to go through all the small
        perfect squares, whereas in Solution2, we have a condition to stop
        searching early.
        """
        dp = list(range(n + 1))
        sqrt, ps = 2, 4
        while ps <= n:
            for i in range(ps, n + 1):
                dp[i] = min(dp[i], dp[i - ps] + 1)
            sqrt += 1
            ps = sqrt**2
        return dp[-1]


sol = Solution3()
tests = [
    (12, 3),
    (13, 2),
    (2278, 3),
]

for i, (n, ans) in enumerate(tests):
    res = sol.numSquares(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
