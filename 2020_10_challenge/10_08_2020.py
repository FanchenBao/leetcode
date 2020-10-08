# from pudb import set_trace; set_trace()
from typing import List
from bisect import bisect_right


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """Standard solution"""
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1


class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        """A bit simpler version. However whether this version is more
        intuitive than the previous one is open for debate.
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2  # left/lower mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left if nums[left] == target else -1


class Solution3:
    def search(self, nums: List[int], target: int) -> int:
        """Cheating solution"""
        idx = bisect_right(nums, target)
        return idx - 1 if idx != 0 and nums[idx - 1] == target else -1
