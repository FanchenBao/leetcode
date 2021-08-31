# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """LeetCode 153

        Binary search. A bit tricky. We have to first check if nums[hi] is
        already the min value. The reason for doing so is that as long as
        nums[0] > nums[-1], we are certain that the min value is on the right
        portion. So it is necessary to always check nums[hi] before doing the
        binary search. During binary search, we compare nums[mid] with nums[0].
        If nums[mid] is larger than nums[0], we are on the left side. So lo =
        mid + 1. Otherwise, we are on the right side, so hi = mid. Note that we
        do not do hi = mid - 1 because we want to make sure that hi stays on the
        right side of the array.

        O(logN), 28 ms, 99% ranking.
        """
        if nums[0] < nums[-1]:
            return nums[0]
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            if nums[hi] < nums[hi - 1]:
                return nums[hi]
            mid = (lo + hi) // 2
            if nums[mid] > nums[0]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]


sol = Solution()
tests = [
    ([3, 4, 5, 1, 2], 1),
    ([4, 5, 6, 7, 0, 1, 2], 0),
    ([11, 13, 15, 17], 11),
    ([2, 4, 5, 6, 7, 0, 1], 0),
    ([1, 2, 4, 5, 6, 7, 0], 0),
    ([0, 1, 2, 4, 5, 6, 7], 0),
    ([7, 0, 1, 2, 4, 5, 6], 0),
    ([6, 7, 0, 1, 2, 4, 5], 0),
    ([5, 6, 7, 0, 1, 2, 4], 0),
    ([2, 1], 1),
    ([1], 1),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.findMin(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
