# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        """Just follow the instruction.

        102 ms, faster than 31.09%
        """
        l = len(nums) // 2
        while l >= 1:
            for j in range(l):
                if j % 2:
                    nums[j] = max(nums[2 * j], nums[2 * j + 1])
                else:
                    nums[j] = min(nums[2 * j], nums[2 * j + 1])
            l //= 2
        return nums[0]


sol = Solution()
tests = [
    ([1,3,5,2,4,8,2,2], 1),
    ([3], 3),
    ([34,54,6,55,4653,4,66,3564,786,675,4,3,22,5,67,869,8,76,54,765,536,7,89,87,65,4,3,65,5,6,6,3], 8),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.minMaxGame(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
