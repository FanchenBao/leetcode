# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter
from bisect import bisect_left


class Solution1:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        """This feels greedy to me.

        First sort nums, and then use two pointers. The best we can hope for is
        that each small value has a pairing big value. This means the small
        value must start from i = 0, and the large value must start from j = 
        len(nums) // 2

        Then we simply progress i and j forward. A few tricks to consider:

        1. each time a value is used, we need to mark it by setting the value in
        nums to zero.
        2. i may catch up to the values used by j. Thus, each time nums[i] is
        zero, we need to keep progressing i.
        3. If i does catch up to j, we basically return to the original position
        and we need to reset the j position.

        O(NlogN), 707 ms, faster than 24.46%
        """
        nums.sort()
        N = len(nums)
        i, j = 0, N // 2
        res = 0
        while j < N:
            while i < j and nums[i] == 0:  # i hit values already used
                i += 1
            if i == j:  # reset j
                j = (N + j) // 2
            while j < N and nums[i] * 2 > nums[j]:
                j += 1
            if j < N:
                res += 2
                nums[i] = nums[j] = 0
                i += 1
                j += 1
        return res


class Solution2:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        """Ref: https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/discuss/3231114/Two-Pointers

        Think from the point of view of the large value. It always progresses,
        but the small value only progress once it fits. This way, we don't have
        to make any additional checks. Also, the large value has to start from
        either the middle if nums have even counts, or middle plus one if nums
        have odd counts.

        O(NlogN), 613 ms, faster than 99.87% 
        """
        N = len(nums)
        nums.sort()
        i = res = 0
        for j in range((N + 1) // 2, N):
            if 2 * nums[i] <= nums[j]:
                res += 2
                i += 1
        return res


sol = Solution2()
tests = [
    ([3,5,2,4], 2),
    ([9,2,5,4], 4),
    ([7,6,8], 0),
    ([67,56,456,56,567,67,678,42,5654,345,342,345,45,456,3], 14),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.maxNumOfMarkedIndices(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
