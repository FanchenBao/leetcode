#! /usr/bin/env python3
"""07/17/2019

A slightly challenging problem. The tricky part is that within each subset,
we allow repetition of elements, but at the subset level, we do not allow
duplicates. My solution is recursive. For any list nums[i], we
compute res = subsetsWithDup(nums[i+1:]), and then figure out the proper way
to incorporate nums[i] into the res. To avoid duplication at subset level, we
check whether nums[i] == nums[i+1] (note that we sort nums to begin with, so
repeated values can be checked by comparing the current value with the one
after it). It nums[i] != nums[i+1], then we need to add nums[i] to all subsets
currently in res, and append the new subset to the end. If not, then we shall
only add nums[i] to the most newly added subsets, because any old subsets
would have already been added to by nums[i+1]. If we add nums[i] again to the
old subsets, we would be creating duplicates. In order to achieve this
functionality, in the recursive call return, we include another variable "pos"
which reports the starting position of appending into res in the previous
recursive call. In other words res[pos:] are the most newly added subsets.

Update:
Solution2 borrowed idea from "https://leetcode.com/problems/subsets-ii/discuss/30168/C%2B%2B-solution-and-explanation".

The essence of this brilliant solution is the observation that the only
difference between this problem and creating power set of unique set of
elements is that for unique set, each element has two options of being incor-
porated into the subsets already created: either incorporated or not. For
non-unique set, each element might have more options: incorporating 0 times,
1 time, 2 times, ... n times. With this observation, we bridge the unique
and non-unique set situations: all elements have n + 1 options for incor-
poration, where n is the number of occurrences of the element in the original
set. To implement this solution is straightforward. We use Counter to count
the occurences of each element, and fill the result list in a nested loop.
"""
from typing import List, Tuple
from collections import Counter


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.helper(nums, 0)[0]

    def helper(
        self, nums: List[int], start: int
    ) -> Tuple[List[List[int]], int]:
        if start == len(nums):
            return [[]], 0
        res, p = self.helper(nums, start + 1)
        curr = nums[start]
        # s is the start position in res where inclusion of curr begins
        s = 0 if p == 0 or curr != nums[start + 1] else p
        size = len(res)  # size serves as the start pos of newly added subsets
        for i in range(s, size):
            res.append(res[i] + [curr])
        return res, size


class Solution2:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        res: List[List[int]] = [[]]
        for k, v in count.items():
            size = len(res)
            for i in range(size):
                for n in range(1, v + 1):
                    res.append(res[i] + [k] * n)
        return res


sol = Solution2()
nums = [2, 2, 3, 3]
print(sol.subsetsWithDup(nums))
