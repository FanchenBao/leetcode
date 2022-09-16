# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution1:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        """MLE
        """
        M, N = len(multipliers), len(nums)
        
        @lru_cache(maxsize=None)
        def dfs(lo: int, idx: int) -> int:
            if idx == M:
                return 0
            hi = N - (idx - lo) - 1
            return max(
                multipliers[idx] * nums[lo] + dfs(lo + 1, idx + 1),
                multipliers[idx] * nums[hi] + dfs(lo, idx + 1),
            )

        return dfs(0, 0)


class Solution2:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        """Worse than solution 1, TLE
        """
        M, N = len(multipliers), len(nums)
        dp = [[-math.inf] * M for _ in range(M)]
        
        def dfs(lo: int, idx: int) -> int:
            if idx == M:
                return 0
            if dp[lo][idx] == -math.inf:
                c1 = multipliers[idx] * nums[lo] + dfs(lo + 1, idx + 1)
                c2 = multipliers[idx] * nums[N - (idx - lo) - 1] + dfs(lo, idx + 1)
                dp[lo][idx] = max(c1, c2)
            return dp[lo][idx]

        return dfs(0, 0)


class Solution3:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        """Bottom up 2D DP, TLE
        """
        M, N = len(multipliers), len(nums)
        dp = [[-math.inf] * M for _ in range(M)]

        for idx in range(M - 1, -1, -1):
            for lo in range(idx + 1):
                hi = N - (idx - lo) - 1
                c1 = multipliers[idx] * nums[lo] + (0 if lo + 1 == M or idx + 1 == M else dp[lo + 1][idx + 1])
                c2 = multipliers[idx] * nums[hi] + (0 if idx + 1 == M else dp[lo][idx + 1])
                dp[lo][idx] = max(c1, c2)

        return dp[0][0]


class Solution4:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        """Bottom up 2D DP, without if/else but with additional column and row

        Exactly the same as official approach 3, TLE
        """
        M, N = len(multipliers), len(nums)
        dp = [[0] * (M + 1) for _ in range(M + 1)]

        for idx in range(M - 1, -1, -1):
            for lo in range(idx + 1):
                hi = N - (idx - lo) - 1
                c1 = multipliers[idx] * nums[lo] + dp[lo + 1][idx + 1]
                c2 = multipliers[idx] * nums[hi] + dp[lo][idx + 1]
                dp[lo][idx] = max(c1, c2)

        return dp[0][0]


class Solution5:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        """Bottom up 1D DP, TLE
        """
        M, N = len(multipliers), len(nums)
        dp = [-math.inf] * M

        for idx in range(M - 1, -1, -1):
            for lo in range(idx + 1):
                hi = N - (idx - lo) - 1
                c1 = multipliers[idx] * nums[lo] + (0 if lo + 1 == M or idx + 1 == M else dp[lo + 1])
                c2 = multipliers[idx] * nums[hi] + (0 if idx + 1 == M else dp[lo])
                dp[lo] = max(c1, c2)

        return dp[0]


class Solution6:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        """Follow https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/discuss/1075448/Python-DP-Clear-the-Cache!

        Clear cache between tests to avoid MLE.

        Does avoid MLE, but nope, got TLE instead.
        """
        M, N = len(multipliers), len(nums)
        
        @lru_cache(maxsize=None)
        def dfs(lo: int, idx: int) -> int:
            if idx == M:
                return 0
            hi = N - (idx - lo) - 1
            return max(
                multipliers[idx] * nums[lo] + dfs(lo + 1, idx + 1),
                multipliers[idx] * nums[hi] + dfs(lo, idx + 1),
            )

        res = dfs(0, 0)
        dfs.cache_clear()
        return res


class Solution7:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        """LeetCode 1770

        Bottom up 1D DP, without if/else

        What a journey!

        * lru_cache memory limit exceeded (MLE)
        * 2D DP top down time limit exceeded (TLE)
        * 2D DP bottom up with if/else, TLE
        * 2D DP bottom up without if/else, but with additional column and row, TLE
        * 1D DP bottom up with if/else, TLE
        * lru_cache with cache clearing, TLE
        * 1D DP bottom up without if/else passed, with very good time.

        Can you believe it? How slow is Python's if/else? Apparently it is very
        slow.

        The problem itself is pretty standard DP. The first breakthrough is to
        realize that for nums, we only need to keep lo. hi can be computed from
        lo and idx.

        The second breakthrough is just being patient and convert the naive DP
        to the most optimal version, which is 1D DP without if/else.

        O(M^2), 3659 ms, faster than 99.82%
        """
        M, N = len(multipliers), len(nums)
        dp = [max(multipliers[M - 1] * nums[lo], multipliers[M - 1] * nums[N - M + lo]) for lo in range(M)]

        for idx in range(M - 2, -1, -1):
            for lo in range(idx + 1):
                hi = N - (idx - lo) - 1
                c1 = multipliers[idx] * nums[lo] + dp[lo + 1]
                c2 = multipliers[idx] * nums[hi] + dp[lo]
                dp[lo] = max(c1, c2)

        return dp[0]


sol = Solution7()
tests = [
    ([1,2,3], [3,2,1], 14),
    ([1,2,4], [2,3,1], 16),
    ([-5,-3,-3,-2,7,1], [-10,-5,3,4,6], 102),
    ([555,526,732,182,43,-537,-434,-233,-947,968,-250,-10,470,-867,-809,-987,120,607,-700,25,-349,-657,349,-75,-936,-473,615,691,-261,-517,-867,527,782,939,-465,12,988,-78,-990,504,-358,491,805,756,-218,513,-928,579,678,10], [783,911,820,37,466,-251,286,-74,-899,586,792,-643,-969,-267,121,-656,381,871,762,-355,721,753,-521], 6861161),
]

for i, (nums, multipliers, ans) in enumerate(tests):
    res = sol.maximumScore(nums, multipliers)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
