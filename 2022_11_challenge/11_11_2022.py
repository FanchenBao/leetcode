# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """LeetCode 26

        Two pointers.

        O(N), 185 ms, faster than 60.77%
        """
        i, j = 0, 0
        while j < len(nums):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1


sol = Solution()
tests = [
    ([7,1,5,3,6,4], 7),
    ([1,2,3,4,5], 4),
    ([7,6,4,3,1], 0),
]

for i, (prices, ans) in enumerate(tests):
    res = sol.maxProfit(prices)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
