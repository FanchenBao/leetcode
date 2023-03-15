# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import chain


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return list(chain(*([int(d) for d in str(n)] for n in nums)))


sol = Solution()
tests = [
    ([13,25,83,77], [1,3,2,5,8,3,7,7]),
    ([7,1,3,9], [7,1,3,9]),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.separateDigits(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
