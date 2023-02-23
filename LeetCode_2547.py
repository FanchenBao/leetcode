# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter
from functools import lru_cache


class Solution1:
    def minCost(self, nums: List[int], k: int) -> int:
        """This is unfair. It passed every test case, but just TLE.
        """
        N = len(nums)
        dp = [[0] * N for _ in range(N)]
        for i in range(N):
            counter = Counter()
            counter[nums[i]] = 1
            trimmed_len = 0
            for j in range(i + 1, N):
                counter[nums[j]] += 1
                if counter[nums[j]] == 2:
                    trimmed_len += 2
                elif counter[nums[j]] > 2:
                    trimmed_len += 1
                dp[i][j] = trimmed_len
        
        @lru_cache(maxsize=None)
        def helper(idx: int) -> int:
            if idx == N:
                return 0
            res = math.inf
            for i in range(idx, N):
                res = min(res, dp[idx][i] + k + helper(i + 1))
            return res

        return helper(0)


class Solution2:
    def minCost(self, nums: List[int], k: int) -> int:
        """This is bottom up. You'd better not TLE this one.

        Luckily, this did not TLE, but the runtime is pretty bad.

        O(N^2), 9244 ms, faster than 7.84% 
        """
        N = len(nums)
        dp_trim = [[0] * N for _ in range(N)]
        for i in range(N):
            counter = Counter()
            counter[nums[i]] = 1
            trimmed_len = 0
            for j in range(i + 1, N):
                counter[nums[j]] += 1
                if counter[nums[j]] == 2:
                    trimmed_len += 2
                elif counter[nums[j]] > 2:
                    trimmed_len += 1
                dp_trim[i][j] = trimmed_len

        dp_price = [math.inf] * (N + 1)
        dp_price[-1] = 0
        for i in range(N - 1, -1, -1):
            for j in range(i, N):
                dp_price[i] = min(dp_price[i], dp_trim[i][j] + k + dp_price[j + 1])
        return dp_price[0]


sol = Solution2()
tests = [
    ([1,2,1,2,1,3,3], 2, 8),
    ([1,2,1,2,1], 2, 6),
    ([1,2,1,2,1], 5, 10),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.minCost(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
