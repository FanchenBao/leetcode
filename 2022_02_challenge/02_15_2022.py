# from pudb import set_trace; set_trace()
from typing import List
from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """LeetCode 136

        I remember this problem. XOR is the way to go.

        O(N) time, O(1) space, 146 ms, 68% ranking.
        """
        return reduce(lambda pre, cur: pre ^ cur, nums)


sol = Solution()
tests = [
    ([2, 2, 1], 1),
    ([4, 1, 2, 1, 2], 4),
    ([1], 1)
]

for i, (nums, ans) in enumerate(tests):
    res = sol.singleNumber(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
