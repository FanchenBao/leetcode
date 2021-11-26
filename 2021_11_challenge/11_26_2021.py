# from pudb import set_trace; set_trace()
from typing import List
import bisect


class Solution1:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """LeetCode 35

        Basic binary search.

        O(logN), 53 ms, 29% ranking.
        """
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo


class Solution2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_right(nums, target)
        return idx if nums[idx - 1] != target else idx - 1
        

sol = Solution2()
tests = [
    ([1, 3, 5, 6], 5, 2),
    ([1, 3, 5, 6], 2, 1),
    ([1, 3, 5, 6], 7, 4),
    ([1, 3, 5, 6], 0, 0),
    ([1, 3, 5, 6], 1, 0),
    ([1, 3, 5, 6], 3, 1),
    ([1, 3, 5, 6], 5, 2),
    ([1, 3, 5, 6], 6, 3),
    ([1], 0, 0),
]

for i, (nums, target, ans) in enumerate(tests):
    res = sol.searchInsert(nums, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
