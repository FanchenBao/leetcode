# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def findPeakElement(self, nums: List[int]) -> int:
        """LeetCode 162

        The first downward signifies the existence of a peak. We can do this
        in O(N), 40 ms, 92% ranking.
        """
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return i - 1
        return len(nums) - 1


class Solution2:
    def findPeakElement(self, nums: List[int]) -> int:
        """Binary search

        O(logN), 48 ms, 51% ranking.
        """
        n = len(nums)
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid + 1] < nums[mid]:
                hi = mid
            else:
                lo = mid + 1
        return lo


sol = Solution2()
tests = [
    ([1, 2, 3, 1], {2}),
    ([1, 2, 1, 3, 5, 6, 4], {1, 5}),
    ([3, 1, 2, 3], {0, 3}),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.findPeakElement(nums)
    if res in ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
