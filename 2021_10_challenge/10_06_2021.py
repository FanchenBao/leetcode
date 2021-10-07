# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """LeetCode 442

        We use swap to put one value to its correct position. After that, we
        remain at the front and keep swapping until the front value is either -1
        which means we have encountered a duplicate, or the front value is in
        the correct position. When either of these two scenarios happen, we move
        the front pointer forward until hitting a new wrong position.

        O(2N) time and O(1) space. 416 ms, 35% ranking.
        """
        i, n = 0, len(nums)
        res = []
        while i < n:
            while i < n and (nums[i] == -1 or nums[i] == i + 1):
                i += 1
            while i < n and nums[i] != -1 and nums[i] != i + 1:
                ni = nums[i] - 1
                if nums[i] != nums[ni]:
                    nums[i], nums[ni] = nums[ni], nums[i]
                else:
                    res.append(nums[i])
                    nums[i] = -1
        return res


class Solution2:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """This is the good solution from the last time I attempted this problem
        The idea is to mark in nums which position can be correctly fulfilled
        without actually making the swap. We can set the num value to negative
        to indicate that there is a correct value for the position where the
        current num resides. Duplicate is detected if the current value's
        correct position is negative (this means that position has been occupied
        already)
        """
        res = []
        for n in nums:
            if nums[abs(n) - 1] < 0:
                res.append(abs(n))
            else:
                nums[abs(n) - 1] *= -1
        return res


sol = Solution2()
tests = [
    ([4, 3, 2, 7, 8, 2, 3, 1], [2, 3]),
    ([1, 1, 2], [1]),
    ([1], []),
    ([2, 1], []),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.findDuplicates(nums)
    if sorted(res) == sorted(ans):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
