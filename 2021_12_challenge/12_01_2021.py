# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """LeetCode 198

        Standard DP.

        O(N), 32 ms, 70% ranking.

        UPDATE: I don't even need a res, because the robbing later houses will
        always achieve more value than robbing earlier houses.
        """
        pp, p = 0, 0
        for n in nums:
            p, pp = max(pp + n, p), p
        return p


sol = Solution()
tests = [
    ([1,2,3,1], 4),
    ([2,7,9,3,1], 12),
    ([2,1,1,2], 4),
    ([1], 1),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.rob(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
