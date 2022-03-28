# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """LeetCode 81

        The key is to remove the duplicates at both ends of the nums. By doing
        this, we can easily determine whether a given number is on the left
        or right half of the rotation. Then use binary search. If nums[mid]
        and target are on the same side, we simply perform binary search within
        that side. Otherwise, we move lo or hi to approach the current side of
        the target.

        O(logN) on average. Worst case O(N) where all values in nums are the
        samel.
        """
        if target == nums[0] or target == nums[-1]:
            return True
        if nums[-1] < target < nums[0]:
            return False
        l, r = 0, len(nums) - 1
        while l < r and nums[l] == nums[r]:  # remove duplicates at both ends of nums
            l += 1
            r -= 1
        target_side = 'l' if target > nums[r] else 'r'
        lo, hi = l, r
        while lo < hi:
            mid = (lo + hi) // 2
            mid_side = 'l' if nums[mid] > nums[r] else 'r'
            if target_side == mid_side:
                if nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            else:
                if mid_side == 'l':
                    lo = mid + 1
                else:
                    hi = mid
        return nums[lo] == target


sol = Solution()
tests = [
    ([2,5,6,0,0,1,2], 0, True),
    ([2,5,6,0,0,1,2], 3, False),
    ([1,1,1,0,1,1], 0, True),
    ([1], 0, False),
    ([3,5,1], 5, True),
]

for i, (nums, target, ans) in enumerate(tests):
    res = sol.search(nums, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
