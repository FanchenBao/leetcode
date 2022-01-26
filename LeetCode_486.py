# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache


class Solution1:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        """Recursion with memoization.

        The very important trick is at the end, the winning condition is
        different depending on whether there are even or odd number of items
        to pick. If there are even number of items, then the last recursion
        happens with p1_score indeed corresponding to the first player. Thus,
        the winning condition is p1_score >= p2_score.

        If there are odd number of items, then the last recursion happens with
        p1_score corresponding to the second player. Thus, the winning
        condition must exclude the equal sign.

        O(2^N), 193 ms, 23% ranking.
        """
        sum_total = sum(nums)
        size = len(nums)

        @lru_cache(maxsize=None)
        def helper(state: int, p1_score: int, p2_score: int) -> bool:
            if state == (1 << size) - 1:
                return p1_score > p2_score if size % 2 else p1_score >= p2_score
            for i in range(size):
                if not (state >> i) & 1:
                    break
            for j in range(size - 1, -1, -1):
                if not (state >> j) & 1:
                    break
            if not helper(state | (1 << i), p2_score, p1_score + nums[i]) or not helper(state | (1 << j), p2_score, p1_score + nums[j]):
                return True
            return False

        return helper(0, 0, 0)


class Solution2:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        """DP top down from the official solution.

        This is much clearer than solution1. No trick needed.

        O(N^2), 36 ms.
        """

        @lru_cache(maxsize=None)
        def dp(lo: int, hi: int) -> int:
            """Find the max score the first player can get given the subarray
            nums[lo:hi + 1].

            The player can choose nums[lo], which leavs the other player
            nums[lo + 1:hi + 1] to choose. Since the two players are playing
            against each other, we record the net score, i.e. the score the
            first player can get minus the max score the second player can get.

            NOTE that the first and second players are only discussed within
            the context of each recursion, not the ACTUAL first and second
            player.
            """
            if lo == hi:
                return nums[lo]
            return max(nums[lo] - dp(lo + 1, hi), nums[hi] - dp(lo, hi - 1))

        return dp(0, len(nums) - 1) >= 0


class Solution3:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        """DP bottom up, 1D array from the official solution.

        Draw the 2D DP table out, fill it from bottom right corner up. At each
        row, fill from left to right starting from the diagonal position.

        Once the 2D DP procedure is clear, it is not hard to see that it can
        be converted to 1D. IMPORTANT: the dp table must be independent of nums

        O(N^2)
        """
        N = len(nums)
        dp = nums[:]
        for lo in range(N - 2, -1, -1):
            for hi in range(lo + 1, N):
                dp[hi] = max(nums[lo] - dp[hi], nums[hi] - dp[hi - 1])
        return dp[-1] >= 0

        

sol = Solution3()
tests = [
    ([1, 5], True),
    ([1,5,2], False),
    ([1,5,233,7], True),
    ([0], True),
    ([1,3,1], False),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.PredictTheWinner(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
