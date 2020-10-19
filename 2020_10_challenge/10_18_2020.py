# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """88% ranking.

        This is a hodgepodge kind of solution. We first perform
        a solution for unlimited number of transactions. If 2 * k
        >= number of prices, we have unlimited number of transactions.

        If this we don't have unlimited transactions, we use k + 1
        state machines. We run through all the state machines to simulate
        maximum k transactions. This part runs in O(kN) time.
        
        Although this solution passed the OJ, it actually timed
        out when k is slightly smaller than the number of
        transactions under unlimited situation. e.g. when
        the number of transactions under unlimited situation is
        5000, and we make k 4999.

        Just saw the solution, which provides the same run time as
        my solution: O(N) when we can use unlimited transactions,
        and O(kN) when not. So when k is sufficiently big yet
        below the transactions allowed for unlimited transactions,
        this algorithm won't work.
        """
        # state machine under unlimited transactions
        if 2 * k >= len(prices):
            h, e = -math.inf, 0
            for p in prices:
                h = max(h, e - p)
                e = max(e, h + p)
            return e
        else:
            # state machine with at most k transactions
            hs, es = [-math.inf] * (k + 1), [0] * (k + 1)
            for p in prices:
                for i in range(1, k + 1):
                    hs[i] = max(hs[i], es[i - 1] - p)
                    es[i] = max(es[i], hs[i] + p)
            return es[-1]


sol = Solution1()
tests = [
    (2, [2, 4, 1], 2),
    (2, [3, 2, 6, 5, 0, 3], 7),
    (2, [3, 3, 5, 0, 0, 3, 1, 4], 6),
    (100, [3, 3, 5, 0, 0, 3, 1, 4], 8),
    (100, [3, 2, 6, 5, 0, 3], 7),
    (100, [1, 2, 2, 3, 1, 100], 101),
]

for i, (k, prices, ans) in enumerate(tests):
    res = sol.maxProfit(k, prices)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
