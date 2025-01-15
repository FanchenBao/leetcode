# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def update(
        self,
        pre: int,
        j: int,
        hi: int,
        dp: List[List[int]],
        last_indices: List[int],
    ) -> int:
        if 0 < pre <= hi and last_indices[pre] >= 0:
            k = last_indices[pre]
            return dp[k][j] + 1
        return 0

    def longestSubsequence(self, nums: List[int]) -> int:
        """
        Use DP, where dp[i][j] is the longest subseq length ending at nums[i]
        with abs diff not smaller than j. Note that essentially dp[i] is a
        suffix max of longest subseq length where dp[i][j] is the max of all
        dp[i][j...end]

        When a new nums[i + 1] is considered, we go through all possible diffs.
        For each diff, we have the target number nums[i + 1] - j or nums[i + 1]
        + j. We find the latest indices of these target numbers and query the
        longest subseq length ending at the target number with abs diff not
        smaller than j.

        We can use the latest index because it always offers a longer subseq
        than an earlier index with the same target number.

        O(MN)
        """
        lo, hi = min(nums), max(nums)
        dp = [[0] * (hi - lo + 1) for _ in range(len(nums))]
        last_indices = [-1] * (hi + 1)
        # Edge cases
        for j in range(len(dp[0])):
            dp[0][j] = 1
        last_indices[nums[0]] = 0
        res = 0
        for i in range(1, len(nums)):
            for j in range(hi - lo, -1, -1):
                # previous subseq value bigger than nums[i]
                op1 = self.update(nums[i] + j, j, hi, dp, last_indices)
                # previous subseq value smaller than nums[i]
                op2 = self.update(nums[i] - j, j, hi, dp, last_indices)
                dp[i][j] = max(op1, op2, dp[i][j + 1] if j < hi - lo else 0)
                res = max(res, dp[i][j])
            last_indices[nums[i]] = i
        return res


sol = Solution()
tests = [
    ([16, 6, 3], 3),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.longestSubsequence(nums)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
