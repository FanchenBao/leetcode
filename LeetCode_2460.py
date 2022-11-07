# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def applyOperations(self, nums: List[int]) -> List[int]:
        """Use two pointers to rearrange in one pass. Overall, we use two passes

        O(N), 113 ms, faster than 33.33%
        """
        for j in range(1, len(nums)):
            if nums[j - 1] == nums[j]:
                nums[j - 1] *= 2
                nums[j] = 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i]:
                i += 1
            elif nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums


class Solution2:
    def applyOperations(self, nums: List[int]) -> List[int]:
        """One pass solution from

        https://leetcode.com/problems/apply-operations-to-an-array/discuss/2783107/One-Pass-C%2B%2BJavaPython3

        My original one-pass attempt didn't work, because I was trying to
        move zeros along with the operation. However, the operation would change
        if we move zeros around. Thus, I gave it up.

        This one pass solution does not concern with zeros. Instead, it just
        fling the non-zeros to the front. By doing so, we automatically separate
        the zeros to the end.

        O(N), one pass. 118 ms, faster than 33.33%
        """
        i = 0
        for j in range(len(nums) - 1):
            if nums[j] == nums[j + 1]:
                nums[j] *= 2
                nums[j + 1] = 0
            if nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        if nums[-1]:  # handle edge case such as [0, 1]
            nums[i], nums[-1] = nums[-1], nums[i]
        return nums


sol = Solution2()
tests = [
    ([1,2,2,1,1,0], [1,4,2,0,0,0]),
    ([0,1], [1, 0]),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.applyOperations(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
