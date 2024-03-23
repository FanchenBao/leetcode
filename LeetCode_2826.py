# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """
        DP(idx, prev) represents the number of min operations to make
        nums[idx:] with the previous group chosen as prev satisfy the
        requirement.

        The requirement is to turn nums into a non-decreasing arrangement of
        1, 2, and 3.

        Thus, for each DP(idx, prev), depending on what the prev is, we can
        pick different values for the current. If prev == 1, we can choose
        1, 2, 3 for the current. If prev == 2, we can only choose 2 or 3. If
        prev == 3, we only have 3 as the choice.

        For the answer, we return DP(0, 1)

        O(3N), 309 ms, faster than 25.45%
        """
        N = len(nums)

        @lru_cache(maxsize=None)
        def dp(idx: int, prev: int) -> int:
            if idx == N:
                return 0
            res = N + 1
            for cur in range(prev, 4):
                res = min(res, int(nums[idx] != cur) + dp(idx + 1, cur))
            return res

        return dp(0, 1)


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
