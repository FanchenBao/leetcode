# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import accumulate
from functools import lru_cache


class Solution1:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        """LeetCode 486

        Find the max score each player can get given the current array state.
        We can use a prefix sum to quickly find the remaining score a player can
        take if the other player scores optimally.

        O(N^2), 44 ms, faster than 92.84% 
        """
        psum = list(accumulate(nums, initial=0))

        @lru_cache(maxsize=None)
        def dp(lo: int, hi: int) -> int:
            if lo == hi:
                return nums[lo]
            return max(
                nums[lo] + psum[hi + 1] - psum[lo + 1] - dp(lo + 1, hi),
                nums[hi] + psum[hi] - psum[lo] - dp(lo, hi - 1),
            )

        p1 = dp(0, len(nums) - 1)
        p2 = psum[-1] - p1
        return p1 >= p2


class Solution2:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        """Another way to think about this, according to the official solution,
        is to maximize the score difference between player 1 and player 2 at
        each nums state. We call dp(lo, hi) as the max score diff between the
        two players. This way, we don't even have to use prefix sum.

        Another trick is to realize that if the length of nums is even, player 1
        is always going to win. We can color nums as RBRBRB... with the same
        number of Rs and Bs. Then we find the sum of all Rs and all Bs. Player
        1 just needs to pick the color with the largest sum, then player 2 will
        be forced to pick the other color. Thus, player 1 always wins.

        O(N^2), 42 ms, faster than 95.15% 
        """

        @lru_cache(maxsize=None)
        def dp(lo: int, hi: int) -> int:
            # max score diff for player 1
            if lo == hi:
                return nums[lo]
            return max(nums[lo] - dp(lo + 1, hi), nums[hi] - dp(lo, hi - 1))

        return len(nums) % 2 == 0 or dp(0, len(nums) - 1) >= 0


        

sol = Solution2()
tests = [
    ([1,5,2], False),
    ([1,5,233,7], True),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.PredictTheWinner(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
