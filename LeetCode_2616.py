# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter
from functools import lru_cache
from bisect import bisect_right


class Solution1:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        """TLE
        """
        if p == 0:
            return 0
        nums.sort()
        dp1, dp2 = [math.inf] * (p + 1), [math.inf] * (p + 1)
        dp1[0] = 0
        dp2[0] = 0
        N = len(nums)
        for i in range(len(nums) - 2, -1, -1):
            tmp = [math.inf] * (p + 1)
            tmp[0] = 0
            for j in range(1, min(p, (N - i) // 2) + 1):
                tmp[j] = min(max(nums[i + 1] - nums[i], dp2[j - 1]), dp1[j])
            dp1, dp2 = tmp, dp1
        return dp1[p]


class Solution2:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        """TLE
        """
        if p == 0:
            return 0
        nums.sort()
        N = len(nums)

        @lru_cache(maxsize=None)
        def dp(idx: int, rem: int) -> int:
            if idx >= N:
                return 0
            if rem == 0:
                return 0
            if rem > (N - idx) // 2:
                return math.inf
            return min(max(nums[idx + 1] - nums[idx], dp(idx + 2, rem - 1)), dp(idx + 1, rem))

        return dp(0, p)


class Solution3:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        """Binary search. Create a sorted array of diffs between adjacent values
        Pick a max diff, then binary search to find the range where all the diffs
        are smaller than max diff. Then go through that range to see if there
        can be at least p number of pairs. If there are, we can shrink the max
        diff, otherwise we cannot.

        Another tricky part is to count the max number of pairs in the range of
        all pairs whose diffs are smaller than the max diff picked. To do so,
        we sort again based on the each pair's starting index, and count
        greedily.

        O(NlogN + log(max(nums)) * Nlog(N)), 2542 ms, faster than 5.14%
        """
        if p == 0:
            return 0
        nums.sort()
        sorted_diffs = sorted((nums[i + 1] - nums[i], i) for i in range(len(nums) - 1))
        lo, hi = 0, nums[-1] + 1
        while lo < hi:
            mid = (lo + hi) // 2
            idx = bisect_right(sorted_diffs, mid, key=lambda tup:tup[0])
            used = []  # a list of starting indices of all pairs
            for i in sorted(sorted_diffs[j][1] for j in range(idx)):
                if not used or i - 1 != used[-1]:  # check whether an index has been used already
                    used.append(i)
            if len(used) >= p:
                hi = mid
            else:
                lo = mid + 1
        return lo
        


sol = Solution3()
tests = [
    ([10,1,2,7,1,3], 2, 1),
    ([4,2,1,2], 1, 0),
    ([1,1,0,3], 2, 2),
]

for i, (nums, p, ans) in enumerate(tests):
    res = sol.minimizeMax(nums, p)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
