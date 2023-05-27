# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        """LeetCode 837

        It's quite complex. A lot of analysis. The basic idea is DP and prefix
        sum. The analysis is the size between k and maxPts. If k is larger or
        equal to maxPts, we first fill up prefix sum to maxPts, and then to k.
        Otherwise, we fill up to k directly.

        Then we need to fill up to n, but here is another analysis, because n
        can be smaller than maxPts.

        Finally, the edge case is when n or k is equal to zero, in which case
        we always return 1.

        O(N), 107 ms, faster than 26.27%
        """
        if n * k == 0:  # if n == 0, whatever Alice draws works. If k == 0, Alice does not draw, then whatever n works
            return 1
        presum = [0]
        if k >= maxPts:
            # phase 1: up till maxPts
            for i in range(1, maxPts + 1):
                cur = 1 / maxPts + 1 / maxPts * presum[-1]
                presum.append(presum[-1] + cur)
            # phase 2: up till k
            for i in range(maxPts + 1, k + 1):
                cur = 1 / maxPts * (presum[-1] - presum[-1 - maxPts])
                presum.append(presum[-1] + cur)
        else:
            for i in range(1, k + 1):
                cur = 1 / maxPts + 1 / maxPts * presum[-1]
                presum.append(presum[-1] + cur)
        # phase 3: up till n
        for i in range(k + 1, min(n, k - 1 + maxPts) + 1):
            if i - maxPts - 1 < 0:
                cur = 1 / maxPts + 1 / maxPts * presum[k - 1]
            else:
                cur = 1 / maxPts * (presum[k - 1] - presum[i - maxPts - 1])
            presum.append(presum[-1] + cur)
            if i == n:
                return presum[i] - presum[k - 1]
        return presum[-1] - presum[k - 1]


class Solution2:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        """This is my version of converting the naive O(N * maxPts) solution
        from the official solution.

        It's still quite a struggle to get the indices correct during presum.

        O(N), 171 ms, faster than 6.96%
        """
        presum = [0, 1]  # presum[i] is the sum of prob from 0 to i - 1
        # Also set up presum[1] = 1 means the prob of getting 1 - 1 = 0 is 1.
        for i in range(1, n + 1):  # find the prob of getting exactly i
            if k - 1 + maxPts < i:
                # the max we can use in previous formation is k - 1. The max we
                # can take is maxPts. It k - 1 + maxPts < i, we cannot make i
                break
            # we can take previously made probability from max(0, i - maxPts)
            # to min(k - 1, i - 1). Use prefix sum to get the sum of all these
            # probs
            cur = (presum[min(k - 1, i - 1) + 1] - presum[max(0, i - maxPts)]) / maxPts
            presum.append(presum[-1] + cur)
        return presum[-1] - presum[k]

        
        

sol = Solution2()
tests = [
    (10, 1, 10, 1.00),
    (6, 1, 10, 0.600),
    (21, 17, 10, 0.73278),
    (10, 10, 10, 0.23579),
    (0, 0, 1, 1.000),
    (1, 0, 100, 1.000),
    (421, 400, 47, 0.71188),
]

for i, (n, k, maxPts, ans) in enumerate(tests):
    res = sol.new21Game(n, k, maxPts)
    if math.isclose(res, ans, rel_tol=1e-04):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
