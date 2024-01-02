# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        """
        dp[i] is the max number of steps to jump from nums[0] to
        nums[i].

        One important thing to note is that as we perform dp, if
        a previous nums[j] can be used to jump to nums[i], yet
        dp[j] is 0, that means it is not possible to jump from
        nums[0] to nums[j], which means the jump from nums[j]
        to nums[i], though allowed by target, is impossible.

        O(N^2), 905 ms, faster than 7.41%
        """
        N = len(nums)
        dp = [0] * N
        for i in range(1, N):
            for j in range(i - 1, -1, -1):
                if abs(nums[j] - nums[i]) <= target and (j == 0 or dp[j] > 0):
                    dp[i] = max(dp[i], 1 + dp[j])
        return dp[-1] if dp[-1] > 0 else -1



sol = Solution()
tests = [
    ([0,2,1,3], 1, -1),
]

for i, (nums, target, ans) in enumerate(tests):
    res = sol.maximumJumps(nums, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
