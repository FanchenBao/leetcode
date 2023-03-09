# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        N = len(nums)
        # num_smaller[i][j] is the number of vals smaller than nums[i] to the
        # left of nums[j]
        num_smaller = [[0] * N for _ in range(N)]
        # num_larger[i][j] is the number of vals bigger than nums[i] to the
        # right of nums[j]
        num_larger = [[0] * N for _ in range(N)]
        for i in range(N):
            pre = 0
            for j in range(i + 1):
                num_smaller[i][j] = pre + int(nums[j] < nums[i])
                pre = num_smaller[i][j]
        for i in range(N - 1, -1, -1):
            pre = 0
            for j in range(N - 1, i - 1, -1):
                num_larger[i][j] = pre + int(nums[j] > nums[i])
                pre = num_larger[i][j]
        # find j, k of the triplet i, j, k, l, such that nums[j] > nums[k]

        # for j in range(1, N - 2):
        #     for k in range(j + 1, N - 1):
        #         if nums[j] > nums[k]:
        #             print(nums[j], nums[k], num_smaller[k], num_larger[j])
        return sum(num_smaller[k][j] * num_larger[j][k] for j in range(1, N - 2) for k in range(j + 1, N - 1) if nums[j] > nums[k])


sol = Solution()
tests = [
    ([1,3,2,4,5], 2),
    ([1,2,3,4], 0),
    ([1,3,5,2,4], 1),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.countQuadruplets(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
