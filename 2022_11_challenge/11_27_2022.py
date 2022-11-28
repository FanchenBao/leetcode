# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict, Counter


class Solution1:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """LeetCode 446

        Use DP. dp[i] is a dict that records the number of arithmetic subseq
        with difference d. For instance, if dp[i] = {d: [1,2]}, that means
        ending at nums[i], with difference d, we have one subsequence with
        length two, and two subsequences with length more than two.

        Then, when we handle nums[i + 1], we go through nums[i], nums[i - 1], ...
        nums[0]. For each num, we get its difference d, and check dp[i][d]
        for the total number of arithmetic subsequences with length two or more.
        Since we are including nums[i + 1], both subsequences with length two or
        more can be included in the number of arithmetic subsequences with length
        two or more for dp[i + 1]. Then we of course also collect the number of
        arithmetic subsequences with length two for dp[i + 1]

        The final result is the sum of the number of arithmetic subsequences
        with length more than two for all numbers and all differences.

        O(N^2), 3098 ms, faster than 27.81%
        """
        dp = [{}]
        N = len(nums)
        for i in range(1, N):
            cur = {}
            for j in range(i - 1, -1, -1):
                d = nums[i] - nums[j]
                # 1 subsequence with two values between nums[i] and nums[j],
                # 0 subsequence with more than two values containing nums[i]
                # and nums[j]
                if d not in cur:
                    cur[d] = [0, 0]
                cur[d][0] += 1
                if d in dp[j]:
                    cur[d][1] += sum(dp[j][d])
            dp.append(cur)
        return sum(v[1] for t in dp for v in t.values())


class Solution2:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """Same solution but we don't have to split the count of arithmetic
        subsequences of different size into a list. They can be combined.

        O(N^2), 2540 ms, faster than 39.05%
        """
        N = len(nums)
        dp = [Counter() for _ in range(N)]
        res = 0
        for i in range(1, N):
            for j in range(i - 1, -1, -1):
                d = nums[i] - nums[j]
                res += dp[j][d]  # total number of arithmetic subseq, two or more in length
                dp[i][d] += dp[j][d] + 1  # the plus one is for the two-length subseq
        return res


sol = Solution2()
tests = [
    ([2,4,6,8,10], 7),
    ([7,7,7,7,7], 16),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.numberOfArithmeticSlices(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
