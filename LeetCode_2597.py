# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        

sol = Solution()
tests = [
    # ([2,4,6], 2, 4),
    # ([1], 1, 1),
    # ([4,2,5,9,10,3], 1, 23),
    ([10,4,5,7,2,1], 3, 23),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.beautifulSubsets(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
