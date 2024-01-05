# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import accumulate


class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        """
        Fail

        Have to read the solution and here is lee215's version

        https://leetcode.com/problems/apply-operations-to-make-all-array-elements-equal-to-zero/discuss/3739101/JavaC%2B%2BPython-Greedy-%2B-Sliding-Window

        For nums[i], to ensure that nums[i] can be reduced to 0, we need to know how
        much needs to be removed from nums[i] when all the values to its left are reduced
        to zero. Since only the k - 1 counts of numbers to the left of nums[i] affect the
        value of nums[i], and the amount reduced is equal to the value of those numbers
        when their predecesors are all zero, thus we keep track of a sum of window of size
        k - 1. If that sum is not bigger than nums[i], then we can reduce nums[i] by that
        amount. Then we reduce the sum by nums[i - k + 1], followed by adding the current
        nums[i] to the sum to form the new sum to check for for nums[i + 1].

        We do this until all nums are visited, and at the end the sum should be zero.

        I don't think I can come up with this with even more time. It is very hard problem
        for me.

        O(N)
        """
        N = len(nums)
        pre = 0
        for i, n in enumerate(nums):
            if pre > n:
                return False
            nums[i] -= pre
            if i - k + 1 >= 0:
                pre -= nums[i - k + 1]
            pre += nums[i]
        return pre == 0


sol = Solution()
tests = [
    ([60,72,87,89,63,52,64,62,31,37,57,83,98,94,92,77,94,91,87,100,91,91,50,26], 4, True),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.checkArray(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
