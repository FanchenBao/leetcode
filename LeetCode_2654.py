# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        num_ones = nums.count(1)
        if num_ones > 0:
            return len(nums) - num_ones
        res = math.inf
        for i in range(1, len(nums) - 1):
            l = math.gcd(nums[i - 1], nums[i])
            r = math.gcd(nums[i], nums[i + 1])
            if l == 1 or r == 1:
                res = len(nums)
            if math.gcd(l, r) == 1:
                res = min(res, len(nums) + 1)
        return res if res < math.inf else -1
        

sol = Solution()
tests = [
    # ([2,6,3,4], 4),
    # ([2,10,6,14], -1),
    # ([1,1], 0),
    # ([6,10,15], 4),
    ([10,5,10,30,70,4,2,6,8,4], 13),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.minOperations(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
