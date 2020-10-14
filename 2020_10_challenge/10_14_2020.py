# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """87% ranking

        Either rob 0 and 2 to len(nums) - 2, or robe 1 to len(nums) - 1
        """
        def rob_linear(start, end):
            p_2, p_1, p = 0, 0, 0
            for i in range(start, end + 1):
                p = max(nums[i] + p_2, p_1)
                p_2, p_1 = p_1, p
            return p

        return max(
            rob_linear(1, len(nums) - 1),
            rob_linear(2, len(nums) - 2) + nums[0],
        )


sol = Solution()
tests = [
    ([2, 3, 2], 3),
    ([1, 2, 3, 1], 4),
    ([0], 0),
    ([1, 43, 45, 6], 49),
    ([2, 1, 1, 2], 3),
    ([1, 1, 1, 2], 3),
    ([1, 1, 3, 6, 7, 10, 7, 1, 8], 25),
    ([2, 2, 4, 3, 2, 5], 10),
    ([2, 4, 3, 2, 5, 2], 10),
    ([4, 3, 2, 5, 2, 2], 10),
    ([3, 2, 5, 2, 2, 4], 10),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.rob(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
