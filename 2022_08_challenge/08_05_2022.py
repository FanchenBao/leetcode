# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """LeetCode 377

        DP. We take the current nums[i] out of target, and ask the question
        how many ways we can form target - nums[i] using nums[i:]. We can DP it
        because we can represent each state by index i and the current target.

        O(N * T), where N = len(nums), T = target. 63 ms, faster than 52.34%
        """
        N = len(nums)

        @lru_cache(maxsize=None)
        def helper(idx: int, tgt: int) -> int:
            if tgt < 0:
                return 0
            if tgt == 0:
                return 1
            res = 0
            for i in range(idx, N):
                res += helper(idx, tgt - nums[i])
            return res

        return helper(0, target)


sol = Solution()
tests = [
    ([1,2,3], 4, 7),
    ([9], 3, 0)
]

for i, (nums, target, ans) in enumerate(tests):
    res = sol.combinationSum4(nums, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
