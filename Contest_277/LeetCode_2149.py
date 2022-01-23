# from pudb import set_trace; set_trace()
from typing import List
from itertools import chain


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [n for n in nums if n > 0]
        neg = [n for n in nums if n < 0]
        return list(chain(*[(p, n) for p, n in  zip(pos, neg)]))


sol = Solution()
tests = [
    ([3,1,-2,-5,2,-4], [3,-2,1,-5,2,-4]),
    ([-1,1], [1, -1]),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.rearrangeArray(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
