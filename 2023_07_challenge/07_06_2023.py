# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import accumulate
from bisect import bisect_right


class Solution1:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """LeetCode 209

        This is binary search

        O(NlogN), 785 ms, faster than 5.02%
        """
        if sum(nums) < target:
            return 0
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            i = s = 0
            for j, n in enumerate(nums):
                s += n
                if j - i + 1 > mid:
                    s -= nums[i]
                    i += 1
                if j - i + 1 == mid:
                    if s >= target:
                        hi = mid
                        break
            else:
                lo = mid + 1
        return lo


class Solution2:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """Prefix sum and binary search

        O(NlogN), 268 ms, faster than 48.05%
        """
        psum = list(accumulate(nums, initial=0))
        if psum[-1] < target:
            return 0
        res = math.inf
        for i, p in enumerate(psum):
            if p >= target:
                idx = bisect_right(psum, p - target)
                if idx > 0:
                    res = min(res, i - idx + 1)
        return res


class Solution3:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """Sliding window for O(N), 264 ms, faster than 59.81%
        """
        res = math.inf
        i = s = 0
        for j, n in enumerate(nums):
            s += n
            while s >= target:
                res = min(res, j - i + 1)
                s -= nums[i]
                i += 1
        return res if res < math.inf else 0


sol = Solution3()
tests = [
    (7, [2,3,1,2,4,3], 2),
    (4, [1,4,4], 1),
    (11, [1,1,1,1,1,1,1,1], 0),
    (1, [2], 1),
    (5, [2,3,1,1,1,1,1], 2),
]

for i, (target, nums, ans) in enumerate(tests):
    res = sol.minSubArrayLen(target, nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
