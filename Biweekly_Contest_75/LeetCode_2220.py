# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return bin(start ^ goal).count('1')


sol = Solution()
tests = [
    ([2,4,1,1,6,5], 3),
    ([6,6,5,5,4,1], 0),
    ([6,6,6], 0),
    ([1,2,3], 0),
    ([1,2,1,2,1,1], 3),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.countHillValley(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
