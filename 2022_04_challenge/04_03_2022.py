# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def reverse(self, nums: List[int], lo: int, hi: int) -> None:
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        LeetCode 31

        I kind of remember the solution to this problem. We search from right
        to left to locate the first element that is smaller than its neighbor
        to the right. This element needs to be swapped by the smallest element
        on the right that is bigger than it. After the swap, we simply reverse
        all the elements on the right.

        O(N), 49 ms, 71% ranking.
        """
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break
        else:
            self.reverse(nums, 0, len(nums) - 1)
            return
        j = i + 1
        while j < len(nums) and nums[j] > nums[i]:
            j += 1
        j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        self.reverse(nums, i + 1, len(nums) - 1)


sol = Solution()
tests = [
    ([1, 2, 3], [1, 3, 2]),
    ([3, 2, 1], [1, 2, 3]),
    ([1, 1, 5], [1, 5, 1]),
]

for i, (nums, ans) in enumerate(tests):
    res = nums[:]
    sol.nextPermutation(res)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
