# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """LeetCode 287.

        HINT. I thought this is the problem solved by exclusive or. But it is
        not. I have to take a look at the hint to realize that the best
        solution is hare and tortoise.

        O(N), 640 ms
        """
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


sol = Solution()
tests = [
    ([1,3,4,2,2], 2),
    ([3,1,3,4,2], 3),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.findDuplicate(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
