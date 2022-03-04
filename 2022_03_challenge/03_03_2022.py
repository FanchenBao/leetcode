# from pudb import set_trace; set_trace()
from typing import List
from itertools import groupby


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """LeetCode 413

        Create a diff array for consecutive elements in nums. Use groupby to
        obtain the length of consecutive same element. From there, we can
        compute the number of arithmatic array in each stretch of consecutively
        equal elements.

        O(N), 84 ms, 5% ranking.
        """
        res = 0
        for _, g in groupby(nums[i] - nums[i - 1] for i in range(1, len(nums))):
            n = len(list(g))
            res += n * (n - 1) // 2
        return res
        

sol = Solution()
tests = [
    ([1,2,3,4], 3),
    ([1], 0),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.numberOfArithmeticSlices(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
