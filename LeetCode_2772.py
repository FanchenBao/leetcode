# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        pre = 0
        
                


sol = Solution()
tests = [
    ([60,72,87,89,63,52,64,62,31,37,57,83,98,94,92,77,94,91,87,100,91,91,50,26], 4, True),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.checkArray(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
