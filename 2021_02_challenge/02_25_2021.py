# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """LeetCode 581

        This is a straightforward method. We first sort the original array to
        obtain the target. Then we compare the original array with the sorted
        version to find the first and last element that do not match. The
        indices of these two elements determine the length pf the unsorted
        subarray. If no such mismatch element exists, that means the original
        array has already been sorted. We return 0.

        O(NlogN), 192 ms, 88% ranking.
        """
        sorted_nums = sorted(nums)
        for i in range(0, len(nums)):
            if nums[i] != sorted_nums[i]:
                break
        else:
            return 0
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] != sorted_nums[j]:
                break
        return j - i + 1


class Solution2:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """This is the O(N) solution. We traverse the list twice. Once from left
        to right and identify the left most element that needs to be changed.
        Then we go from right to left and identify the right most element that
        needs to be changed. Then we done.

        O(N), 204 ms, 68% ranking.

        In the official solution, this one is achieved via a stack. It's the
        same concept, but my solution has O(1) space.
        """
        left = None
        for i in range(0, len(nums) - 1):
            if nums[i + 1] < nums[i]:
                if left is None:
                    left = i - 1
                while left >= 0 and nums[left] > nums[i + 1]:
                    left -= 1
        if left is None:
            return 0
        right = None
        for j in range(len(nums) - 1, 0, -1):
            if nums[j - 1] > nums[j]:
                if right is None:
                    right = j + 1
                while right < len(nums) and nums[right] < nums[j - 1]:
                    right += 1
        return right - left - 1


class Solution3:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """This solution came from a comment. The intuition is that as we go to
        the right, each number should be bigger than the previous one. What we
        need to find is the right most number that is smaller than the max on
        its left side. Similarly, we need to find the left most number that is
        bigger than the min on its right side. These two extremes form the
        boundary.

        """
        cur_max, right = -math.inf, None
        for i in range(len(nums)):
            if nums[i] >= cur_max:
                cur_max = nums[i]
            else:
                right = i
        if right is None:
            return 0
        cur_min, left = math.inf, None
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] <= cur_min:
                cur_min = nums[j]
            else:
                left = j
        return right - left + 1


sol = Solution3()
tests = [
    ([2, 6, 4, 8, 10, 9, 15], 5),
    ([1, 2, 3, 4], 0),
    ([], 0),
    ([5, 4, 3, 2, 1], 5),
    ([5, 4, 3, 3, 1, 2], 6),
    ([3, 4, 1, 2], 4),
    ([1, 2, 10, 3, 4], 3),
    ([1, 3, 2, 2, 2], 4),
    ([3, 4, 1, 2, 5], 4),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.findUnsortedSubarray(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
