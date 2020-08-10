#! /usr/bin/env python3
from typing import List
from random import randint

"""08/05/2019

Solution1:
My solution is to consider the only two configuration of the zig-zag array.
And compute how many decreases needed to achieve each configuration. We return
the min of the two steps as result. Since each move can only be decreasing,
that makes the solution for each config pretty deterministic, i.e. changes can
be made ONLY if a number is too big for its position.

This solution clocked in at 44 ms, 20%

Solution2 (not provided):
From this discussion post:
https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/discuss/350576/JavaC%2B%2BPython-Easy-and-concise

The idea is that the two configuration can be considered like this:
1. All even pos number must be smaller than odd, meaning all even pos number
must be smaller than its adjacent numbers on both side.
2. Similar to above, but all odd pos number must be smaller than its adjacent
numbers on both side.

Apparently, the two configs are very similar can be examined in the same code
with only checking for pos being even or odd. The one benefit of this method
is that we don't have to actually modify the value in nums. This is because
we are only considering decreasing all even pos numbers (config 1) or odd
pos numbers (config 2). When we do a single pass of nums array, changes to the
previous even (odd) pos number will not affect the change to the next even (odd)
number.
"""


class Solution1:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        # A[0] > A[1] < A[2] > A[3] < A[4] > ...
        steps1 = 0
        nums1 = nums[:]
        for i in range(len(nums1) - 1):
            if i % 2 == 0 and nums1[i] <= nums1[i + 1]:
                steps1 += nums1[i + 1] - nums1[i] + 1
                nums1[i + 1] = nums1[i] - 1
            elif i % 2 != 0 and nums1[i] >= nums1[i + 1]:
                steps1 += nums1[i] - nums1[i + 1] + 1
                nums1[i] = nums1[i + 1] - 1
        # A[0] < A[1] > A[2] < A[3] > A[4] < ...
        steps2 = 0
        nums2 = nums[:]
        for i in range(len(nums2) - 1):
            if i % 2 == 0 and nums2[i] >= nums2[i + 1]:
                steps2 += nums2[i] - nums2[i + 1] + 1
                nums2[i] = nums2[i + 1] - 1
            elif i % 2 != 0 and nums2[i] <= nums2[i + 1]:
                steps2 += nums2[i + 1] - nums2[i] + 1
                nums2[i + 1] = nums2[i] - 1
        return min(steps1, steps2)


def test():
    t = 1
    num_len = 1000
    for _ in range(t):
        nums = [randint(1, 1000) for _ in range(num_len)]
        sol = Solution1()
        print(nums)
        print(sol.movesToMakeZigzag(nums))


test()
# nums = [5, 7, 3, 4, 5]
# sol = Solution()
# print(sol.movesToMakeZigzag(nums))
