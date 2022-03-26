# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """LeetCode 704

        O(logN), 307 ms, 58% ranking.
        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo if nums[lo] == target else -1


sol = Solution()
tests = [
    ([-1,0,3,5,9,12], 9, 4),
    ([-1,0,3,5,9,12], 2, -1),
    ([1], 1, 0),
    ([1], 0, -1),
]

for i, (nums, target, ans) in enumerate(tests):
    res = sol.search(nums, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
