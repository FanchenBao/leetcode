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


class Solution4:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        """We do not have to sort based on diff, nor do we have to do an
        additional binary search. We simply sort nums, and go from left to right
        and find the total number of pairs whose diff is smaller or equal to
        the current mid. Greedy is used here, in that we always record the first
        pair that satisfies our requirement. It does not matter if picking the
        first pair would preclude us from picking the immediate next pair that
        shares the value with the previous pair, because among these two pairs,
        we can only get one.

        E.g.: a0, a1, a2. If a1 - a0 and a2 - a1 are both valid, we can either
        pick (a0, a1) or (a1, a2). So which one we pick does not matter in the
        final count. Therefore, we can always pick (a0, a1), and that will make
        the implementation very easy.

        O(Nlog(max(nums))), 1527 ms, faster than 17.81%
        """
        if p == 0:
            return 0
        nums.sort()
        N = len(nums)
        lo, hi = 0, nums[-1] + 1
        while lo < hi:
            mid = (lo + hi) // 2
            num_pairs = i = 0
            while i < N - 1:
                if nums[i + 1] - nums[i] <= mid:  # take pair (i, i + 1)
                    num_pairs += 1
                    # we increment i an additional time to avoid picking i + 1
                    # in the next round. This is the key step of the algo
                    i += 1
                i += 1  # we always increment i
            if num_pairs >= p:
                hi = mid
            else:
                lo = mid + 1
        return lo


sol = Solution4()
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
