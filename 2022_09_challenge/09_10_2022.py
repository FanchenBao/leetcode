# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """LeetCode 188

        We know that this is solved by state machine, but the details are
        always difficult to straighten out. The following points are important

        1. a transaction = one buy and one sell
        2. this means a transaction is also from previous e to current h, and
            then from current h to current e
        3. Therefore, the relationship for e[i] and h[i] is always
            e[i] = max(e[i], h[i] + p) the current empty state always get from the current holding state.
            h[i] = max(h[i], e[i - 1] - p) the current holding state always get from the previous empty state.
        4. edge case h[0] = max(h[0], -p), which means the non-existent state
            e[-1] defaults to 0.
        Then we run through all the prices and we are good.

        O(KPK), 6049 ms, faster than 5.04%
        """
        res = 0
        for num_tran in range(1, k + 1):
            es, hs = [0] * num_tran, [-math.inf] * num_tran
            for p in prices:
                es[0] = max(es[0], hs[0] + p)
                hs[0] = max(hs[0], -p)  # no previous e, thus, we set the profit to -p
                for i in range(1, num_tran):
                    es[i], hs[i] = max(es[i], hs[i] + p), max(hs[i], es[i - 1] - p)
            res = max(res, max(es))
        return res


class Solution2:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """This is O(KP), from my solution 10 months ago

        This is kind of like greedy, because we are saying if we are allowed to
        do k transactions, it is always not worse to do exactly k steps
        than doing k - 1 steps. This works because if max is achieved
        in smaller number of transactions, we can simply do the smaller number
        of transactions and then do nothing to reach k steps in total.

        And we don't have to find max(e), because the last empty state shall
        always have the maximum profit. It either holds the max profit achieved
        previously, or gains profit from the last sell.

        201 ms, faster than 54.61%
        """
        if k == 0:
            return 0
        es, hs = [0] * k, [-math.inf] * k
        for p in prices:
            es[0], hs[0] = max(es[0], hs[0] + p), max(hs[0], -p)
            for i in range(1, k):
                es[i], hs[i] = max(es[i], hs[i] + p), max(hs[i], es[i - 1] - p)
        return es[-1]


sol = Solution2()
tests = [
    (2, [2,4,1], 2),
    (2, [3,2,6,5,0,3], 7),
]

for i, (k, prices, ans) in enumerate(tests):
    res = sol.maxProfit(k, prices)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
