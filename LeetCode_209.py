# from pudb import set_trace; set_trace()
from typing import List
from bisect import bisect_right
from itertools import accumulate
import math


class Solution1:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """Use prefix sum, and binary search at each step, trying to find where
        is the minimal possible subarray to reach a range sum that is larger or
        equal to target.

        O(NlogN), 72 ms, 78% ranking.
        """
        pre_sum = list(accumulate(nums))
        res = math.inf
        for i, s in enumerate(pre_sum):
            if s >= target:
                idx = bisect_right(pre_sum, s - target)
                res = min(res, i - idx + 1)
        return 0 if res == math.inf else res


class Solution2:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """Sliding window for O(N) time, O(N) space
        """
        pre_sum = list(accumulate(nums))
        res = math.inf
        lo = 0
        for hi, s in enumerate(pre_sum):
            if s >= target:
                while lo <= hi and pre_sum[lo] <= s - target:
                    lo += 1
                res = min(res, hi - lo + 1)
        return 0 if res == math.inf else res


class Solution3:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """Better sliding window from the official solution.

        https://leetcode.com/problems/minimum-size-subarray-sum/solution/

        There is no need to create a prefix sum. We simply use one variable to
        accumulate the sum. Once the sum is larger or equal to target, we simply
        deduct the numbers from the start until we reach a subarray whose range
        sum is smaller than target. Then we know the smallest possible range to
        have range sum larger or equal to target.

        O(N) time but O(1) space.
        """
        psum, lo, res = 0, 0, math.inf
        for hi, n in enumerate(nums):
            psum += n
            while psum >= target:
                res = min(res, hi - lo + 1)
                psum -= nums[lo]
                lo += 1
        return 0 if res == math.inf else res


sol = Solution3()
tests = [
    (7,[2,3,1,2,4,3],2),
    (4,[1,4,4],1),
    (11,[1,1,1,1,1,1,1,1],0),
    (15,[1,2,3,4,5],5)
]

for i, (target, nums, ans) in enumerate(tests):
    res = sol.minSubArrayLen(target, nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
