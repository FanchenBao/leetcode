# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution1:
    def longestSquareStreak(self, nums: List[int]) -> int:
        """Sort nums, and check each value. Since we square on each value, it
        will be fast to exhaust all possibilities in nums.

        O(NlogN), 2651 ms, faster than 24.59%
        """
        nums.sort()
        unseen = set(nums)
        res = -1
        for n in nums:
            count = 0
            s = n
            while s in unseen:
                count += 1
                unseen.remove(s)
                s *= s
            if count >= 2:
                res = max(res, count)
        return res


class Solution2:
    def longestSquareStreak(self, nums: List[int]) -> int:
        """DP solution. Might be faster.

        O(NlogN), 2926 ms, faster than 15.45%
        """
        nums.sort()
        dp = Counter()
        for i in range(len(nums) - 1, -1, -1):
            dp[nums[i]] = 1 + dp[nums[i] * nums[i]]
        res = max(dp.values())
        return res if res >= 2 else -1


sol = Solution2()
tests = [
    ([4,3,6,16,8,2], 3),
    ([2,3,5,6,7], -1),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.longestSquareStreak(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
