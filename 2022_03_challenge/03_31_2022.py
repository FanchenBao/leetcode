# from pudb import set_trace; set_trace()
from typing import List
from itertools import accumulate
import math
from functools import lru_cache


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        """LeetCode 410

        I copied the solution to pass the daily challenge, but didn't really
        read it. So this solution still counts as 100% mine. We initially
        failed OJ via TLE. Then I realized that there are a few ways to
        terminate the loop early. Once these conditions are considered, we pass
        the OJ.

        The idea is that we use a recursion function to compute the min of max
        subarray sum from index lo to the end given cuts number of cut. In this
        function, we make a cut at each position from lo towards the end, and
        recurse to find the min max subarray sum of the remaining subarray.
        The early termination happens when there are more cuts than the number
        of elements available in the remaining subarray, or when the sum of
        the current subarray is already larger than what has been achieved
        previously.

        O(N^2M), where N = len(nums), M = m. 3636 ms, 17% ranking.
        """
        presum = list(accumulate(nums))
        n = len(nums)
        
        @lru_cache(maxsize=None)
        def helper(lo: int, cuts: int) -> int:
            if lo == n - 1:
                return nums[lo]
            if cuts == 0:
                return presum[n - 1] - (presum[lo - 1] if lo > 0 else 0)
            res = math.inf
            for i in range(lo + 1, n):
                left_sum = presum[i - 1] - (presum[lo - 1] if lo > 0 else 0)
                if cuts > n - i or left_sum >= res:
                    break
                res = min(res, max(left_sum, helper(i, cuts - 1)))
            return res

        return helper(0, m - 1)


sol = Solution()
tests = [
    ([7,2,5,10,8], 2, 18),
    ([1,2,3,4,5], 2, 9),
    ([1,4,4], 3, 4),
    ([7,2,5,10,8], 3, 14),
    ([1], 0, 1),
]

for i, (nums, m, ans) in enumerate(tests):
    res = sol.splitArray(nums, m)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
