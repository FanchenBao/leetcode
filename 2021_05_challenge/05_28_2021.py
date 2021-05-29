# from pudb import set_trace; set_trace()
from typing import List
import itertools
import collections
import bisect


class Solution1:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """LeetCode 1695

        We use cumulative sum to facilitate the computation of the sum of any
        subarray. We build a idx_map to know what indices any value occupies.
        We keep the indices sorted, such that when a value is encountered as we
        loop through nums, we can use binary search to locate the index of the
        previous occurrence of the current value. When we loop through nums,
        we keep a left pointer and a right pointer. Right pointer always marches
        forward, and each time we will obtain the index of the previous
        occurrence. If the pre index is to the left of the left pointer, that
        means the current value can be included without repetition. Otherwise,
        we must shrink the left pointer to the index right after the pre index.
        As we loop through nums, we keep track of the sum of each valid subarray
        and return the result once nums is depleted.

        O(Nlog(N)), 1552 ms, 17% ranking.
        """
        cumsum = list(itertools.accumulate(nums))
        idx_map = collections.defaultdict(list)
        for i, n in enumerate(nums):
            idx_map[n].append(i)
        l = 0
        res = nums[0]
        for r in range(1, len(nums)):
            val = nums[r]
            pre_i = bisect.bisect_left(idx_map[val], r) - 1
            if pre_i >= 0 and idx_map[val][pre_i] >= l:
                l = idx_map[val][pre_i] + 1
            res = max(res, cumsum[r] - (cumsum[l - 1] if l > 0 else 0))
        return res


class Solution2:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """This is the O(N) solution with sliding window. I have definitely
        seen this before. But unfortunately, my initial goto is still binary
        search.
        """
        i, j = 0, 0
        N = len(nums)
        subarr_set = set()
        res, s = 0, 0
        while i < N and j < N:
            if nums[j] not in subarr_set:
                subarr_set.add(nums[j])
                s += nums[j]
                res = max(res, s)
                j += 1
            else:
                subarr_set.remove(nums[i])
                s -= nums[i]
                i += 1
        return res


sol = Solution2()
tests = [
    ([4, 2, 4, 5, 6], 17),
    ([5, 2, 1, 2, 5, 2, 1, 2, 5], 8),
    ([100, 1, 1, 2, 3, 4, 5, 6], 101),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.maximumUniqueSubarray(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
