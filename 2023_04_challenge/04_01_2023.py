# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """LeetCode 704

        233 ms, faster than 94.24% 
        """
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target:
                hi = mid
            else:
                lo = mid + 1
        return lo - 1 if nums[lo - 1] == target else -1


sol = Solution()
tests = [
    ([5], 5, 0),
]

for i, (nums, target, ans) in enumerate(tests):
    res = sol.search(nums, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
