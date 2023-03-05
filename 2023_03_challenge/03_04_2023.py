# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        """LeetCode 2444

        First of all, all the numbers that is outside [minK, maxK] form
        separators. Thus, we only need to find the total number of subarrays
        within the partitions bounded by the outsiders.

        Within each partition, we find the indices for minK and maxK. If either
        is empty, there is no valid subarray in the partition.

        If both indices arrays exist, we use a merge sort-ish method to find
        the first occuring minK and maxK pair. Let's say minK has index p and
        maxK has index q and p <= q. Let's also assume the start and end indices
        of the partition is lo and hi.

        Then starting from p, we have hi - q + 1 number of valid subarrays.
        Starting from p - 1, we have hi - q + 1 number of valid subarrays.
        ...
        Starting from lo, we have hi - q + 1 number of valid subarrays.

        Thus with p and q as the core pair, we have in total (p - lo + 1) *
        (hi - q + 1) number of valid subarrays.

        Then we move the indices array that has the smaller index forward and
        repeat the same procedure above.

        O(N), 952 ms, faster than 36.34%
        """
        N = len(nums)

        def compute(lo: int, hi: int, min_idx: List[int], max_idx: List[int]) -> int:
            if not min_idx or not max_idx or lo < 0 or lo > hi:
                return 0
            i = j = 0
            res = 0
            pre = lo
            while i < len(min_idx) and j < len(max_idx):
                if min_idx[i] < max_idx[j]:
                    res += (min_idx[i] - pre + 1) * (hi - max_idx[j] + 1)
                    pre = min_idx[i] + 1
                    i += 1
                else:
                    res += (max_idx[j] - pre + 1) * (hi - min_idx[i] + 1)
                    pre = max_idx[j] + 1
                    j += 1
            return res


        lo = -1
        res = 0
        min_idx = []
        max_idx = []
        for i in range(N):
            if nums[i] < minK or nums[i] > maxK:
                res += compute(lo, i - 1, min_idx, max_idx)
                lo = -1
                min_idx.clear()
                max_idx.clear()
            else:
                if lo < 0:
                    lo = i
                if nums[i] == minK:
                    min_idx.append(i)
                if nums[i] == maxK:
                    max_idx.append(i)
        # print(min_idx, max_idx)
        res += compute(lo, N - 1, min_idx, max_idx)
        return res


sol = Solution()
tests = [
    ([1,3,5,2,7,5], 1, 5, 2),
    ([1,1,1,1], 1, 1, 10),
    ([1,1], 1, 1, 3),
]

for i, (nums, minK, maxK, ans) in enumerate(tests):
    res = sol.countSubarrays(nums, minK, maxK)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
