# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        """LeetCode 53

        Kadane's algo. O(N), 983 ms, 17% ranking.
        """
        res, cur = -math.inf, 0
        for n in nums:
            cur = max(n, n + cur)
            res = max(res, cur)
        return res


class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        """Divide and conquer, as requried by the problem description.

        O(NlogN), 2716 ms.
        """

        def dc(lo: int, hi: int) -> int:
            if lo == hi:
                return nums[lo]
            mid = (lo + hi) // 2
            lmax = dc(lo, mid)
            rmax = dc(mid + 1, hi)
            spmaxl, curl = -math.inf, 0
            for i in range(mid, lo - 1, -1):
                curl += nums[i]
                spmaxl = max(spmaxl, curl)
            spmaxr, curr = -math.inf, 0
            for i in range(mid + 1, hi + 1):
                curr += nums[i]
                spmaxr = max(spmaxr, curr)
            return max([lmax, rmax, spmaxl + spmaxr])

        return dc(0, len(nums) - 1)


sol = Solution2()
tests = [
    ([-2,1,-3,4,-1,2,1,-5,4], 6),
    ([1], 1),
    ([5,4,-1,7,8], 23),
    ([-1], -1),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.maxSubArray(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
