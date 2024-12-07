# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        """
        Try each number in nums from large to small and see if it can be the
        outlier. For a number to be outlier, the condition is that the sum of
        the remaining numbers must be even, and half of it must exist in nums

        O(NlogN), 1609 ms, faster than 30.77%
        """
        s = sum(nums)
        nums_counter = Counter(nums)
        nums.sort()
        for n in nums[::-1]:
            q, r = divmod(s - n, 2)
            nums_counter[n] -= 1
            if r == 0 and nums_counter[q] > 0:
                return n
            nums_counter[n] += 1
        return -1  # we shall never reach here


sol = Solution()
tests = [
    ([6, -31, 50, -35, 41, 37, -42, 13], -35),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.getLargestOutlier(nums)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
