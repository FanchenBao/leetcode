# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        pre = nums[0]
        i = 1
        N = len(nums)
        res = 0
        while True:
            while i < N - 1 and nums[i] == nums[i + 1]:
                i += 1
            if i == N - 1:
                break
            if pre < nums[i] and nums[i] > nums[i + 1]:
                res += 1
            elif pre > nums[i] and nums[i] < nums[i + 1]:
                res += 1
            pre = nums[i]
            i += 1
        return res


sol = Solution()
tests = [
    ([2,4,1,1,6,5], 3),
    ([6,6,5,5,4,1], 0),
    ([6,6,6], 0),
    ([1,2,3], 0),
    ([1,2,1,2,1,1], 3),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.countHillValley(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
