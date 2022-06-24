# from pudb import set_trace; set_trace()
from typing import List
from itertools import accumulate


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        """O(N), 968 ms, faster than 93.11%
        """
        presum = list(accumulate(nums))
        return sum(presum[i] >= presum[-1] - presum[i] for i in range(len(nums) - 1))


sol = Solution()
tests = [
    ([10,4,-8,7], 2),
    ([2,3,1,0], 2),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.waysToSplitArray(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
