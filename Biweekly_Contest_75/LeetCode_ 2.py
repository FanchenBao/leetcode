# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        while n > 1:
            for i in range(1, n):
                nums[i - 1] = (nums[i - 1] + nums[i]) % 10
            n -= 1
        return nums[0]


sol = Solution()
tests = [
    ([1, 2, 3, 4, 5], 8),
    ([5], 5)
]

for i, (nums, ans) in enumerate(tests):
    res = sol.triangularSum(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
