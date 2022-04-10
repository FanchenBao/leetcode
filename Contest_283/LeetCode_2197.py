# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        res = [1]
        for i in range(len(nums)):
            n = nums[i]
            gcd = math.gcd(n, res[-1])
            while gcd != 1:
                n = n * res[-1] // gcd
                res.pop()
                gcd = math.gcd(n, res[-1])
            res.append(n)
        return res[1:]


sol = Solution()
tests = [
    ([6,4,3,2,7,6,2], [12, 7, 6]),
    ([2,2,1,1,3,3,3], [2, 1, 1, 3]),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.replaceNonCoprimes(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
