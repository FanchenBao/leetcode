# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution1:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        """LeetCode 1402

        The best scenario for each number of dishes to take is to cook the dish
        with the highest satisfaction the last, the second highest satisfaction
        the second to the last, etc.

        We can obtain the max sum of like-time coeff for each number of dishes.
        Then just obtain the max among them.

        O(N^2), 126 ms, faster than 37.66%
        """
        satisfaction.sort(reverse=True)
        N = len(satisfaction)
        res = 0
        for n in range(N, 0, -1):
            tmp = 0
            for i in range(n):
                tmp += satisfaction[i] * (n - i)
            res = max(res, tmp)
        return res


class Solution2:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        """Same as solution1, but with an early stoppage

        Although this technically is still O(N^2), but early stoppage allows it
        to speed up to 44 ms, faster than 64.24% 
        """
        satisfaction.sort(reverse=True)
        N = len(satisfaction)
        res = -math.inf
        for n in range(N, 0, -1):
            tmp = sum(satisfaction[i] * (n - i) for i in range(n))
            if tmp <= res:
                break
            res = max(res, tmp)
        return res if res > 0 else 0


class Solution3:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        """Top down DP

        O(N^2), 790 ms, faster than 14.24%
        """
        satisfaction.sort()  # a little bit greedy
        N = len(satisfaction)

        @lru_cache(maxsize=None)
        def dp(idx: int, dish: int) -> int:
            if idx == N:
                return 0
            return max(
                satisfaction[idx] * dish + dp(idx + 1, dish + 1),  # take current dish
                dp(idx + 1, dish),  # not take current dish
            )

        return dp(0, 1)


class Solution4:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        """Bottom up DP with O(N) space

        O(N^2) time, 350 ms, faster than 23.10%
        """
        satisfaction.sort()  # a little bit greedy
        N = len(satisfaction)
        dp = satisfaction[:]
        res = 0
        for i in range(2, N + 1):
            tmp = [-math.inf] * N  # cannot be 0, because we need honest coeff
            for j in range(i - 1, N):
                tmp[j] = max(tmp[j - 1], dp[j - 1] + i * satisfaction[j])
            dp = tmp
            res = max(res, dp[-1])
        return res


class Solution5:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        """The real greedy.

        Sort satisfaction from small to large.

        Say we have a, b, c, d, e

        We always want to take e. So let's say we take e as the first dish. We
        have the current coeff as e.

        Then we can try take e as the second dish and d as the first dish. Then
        we have the coeff d + 2e. Notice the difference between the two is d + e
        which is the suffix sum. As long as d + e > 0, we are incrementing the
        total coeff.

        Then we check c + d + e, b + c + d + e, etc. We stop if a suffix sum
        becomes negative. That means any further suffix sum will also be
        negative because satisfaction has been sorted. And a negative suffix sum
        means the total coeff no longer grows. So we stop there and return the
        current total coeff.

        O(NlogN), 43 ms, faster than 69.30% 
        """
        satisfaction.sort()
        res = sufsum = 0
        for i in range(len(satisfaction) - 1, -1, -1):
            sufsum += satisfaction[i]
            if sufsum <= 0:
                break
            res += sufsum
        return res


sol = Solution5()
tests = [
    ([-1,-8,0,5,-9], 14),
    ([4,3,2], 20),
    ([-1,-4,-5], 0),
]

for i, (satisfaction, ans) in enumerate(tests):
    res = sol.maxSatisfaction(satisfaction)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
