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

        O(MN), 11240 ms, 37.40%
        """
        lo, hi = min(nums), max(nums)
        # Every number can form a subsequence with itself, thus the
        # default value for dp is one
        dp = [[1] * (hi - lo + 1) for _ in range(len(nums))]
        last_indices = [-1] * (hi + 1)
        last_indices[nums[0]] = 0
        res = 0
        for i in range(1, len(nums)):
            for j in range(hi - lo, -1, -1):
                # previous subseq value bigger than nums[i]
                op1 = self.update(nums[i] + j, j, hi, dp, last_indices)
                # previous subseq value smaller than nums[i]
                op2 = self.update(nums[i] - j, j, hi, dp, last_indices)
                dp[i][j] = max(op1, op2, dp[i][j + 1] if j < hi - lo else 1)
                res = max(res, dp[i][j])
            last_indices[nums[i]] = i
        return res


class Solution2:
    def longestSubsequence(self, nums: List[int]) -> int:
        """
        This solution is inspired by https://leetcode.com/problems/longest-subsequence-with-decreasing-adjacent-difference/solutions/6230182/simple-dynamic-programming-approach

        It uses the same concept but the meaning of DP is different. Here
        dp[i][j] = longest subseq length starting from NUMBER i with j abs
        difference. For the current number, we go through all possible next
        numbers. For each next number, we have an absolute difference. Then
        to find the max subseq length of the next number, we use dp[next][diff]

        O(MN), 9684 ms, 58.56%
        """
        dp = [[0] * 301 for _ in range(301)]
        # go from right to left and remember to set each dp[i] to be prefix max
        for i in range(len(nums) - 1, -1, -1):
            n = nums[i]
            for nn in range(1, 301):
                diff = abs(n - nn)
                dp[n][diff] = max(dp[n][diff], dp[nn][diff] + 1)
            for j in range(1, len(dp[n])):
                dp[n][j] = max(dp[n][j], dp[n][j - 1])
        return max(max(row) for row in dp)


sol = Solution()
tests = [
    # ([16, 6, 3], 3),
    ([42, 65, 32, 2], 3),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.longestSubsequence(nums)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
