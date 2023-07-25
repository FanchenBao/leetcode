# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import accumulate


class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        nums.sort()
        psum = list(accumulate(nums))
        ssum = list(accumulate(n**2 for n in nums[::-1]))[::-1]
        res = 0
        for n in nums:
            res = (res + n**3) % MOD
        pre = 0
        for i in range(len(psum) - 1):
            pre += psum[i]
            res = (res + pre * ssum[i + 1]) % MOD
        return res


sol = Solution()
tests = [
    ([2,1,4], 141),
    ([1,1,1], 7),
    ([1,1,1,1], 15),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.sumOfPower(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
