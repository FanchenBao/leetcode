# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache


class Solution1:
    def maxCoins(self, nums: List[int]) -> int:
        """LeetCode 312

        Oof, I wasn't able to solve it a year ago. Nor am I able to solve it
        now. It is hard because it is difficult for me to see how the problem
        can be divived into subproblems. Usually, when I encounter a DP problem
        I always think: pick some value as the first step, and then figure out
        how the remaining problem can be solved as a subproblem. This mindset
        reinforces that the first pick is the FIRST step. However, in this
        problem, if we treat the first pick as the first step, we will have
        altered the input array, which makes DP impossible, because the indices
        change. Unfortunately, even though I realized this, I was not able to
        make the mental leap to try treating the first pick as the LAST step.
        The benefit of doing this is that the input array will NOT change after
        the first pick. Then we can split the problem into two stable
        subproblems, and the solution is quite straightforward from there.

        O(N^3), which is not obvious from the top down solution, but quite
        obvious from the bottom up solution.

        11144 ms, 30% ranking. This is almost 20x slower than the same solution
        submitted a year ago. Since there is no change in the number of test
        cases (both occasions, there are 70), my guess is that some test cases
        have been updated.
        """
        new_nums = [1] + [n for n in nums if n] + [1]  # always remove 0s first

        @lru_cache(maxsize=None)
        def helper(lo: int, hi: int) -> int:
            if lo + 1 == hi:  # we only have guards in this range, no number
                return 0
            max_coin = 0
            for i in range(lo + 1, hi):  # new_nums[i] as the LAST to pick
                max_coin = max(
                    max_coin,
                    new_nums[lo] * new_nums[i] * new_nums[hi] + helper(lo, i) + helper(i, hi)  # i becomes the guard
                )
            return max_coin


        return helper(0, len(new_nums) - 1)


class Solution2:
    def maxCoins(self, nums: List[int]) -> int:
        """Bottom up. The infamous DP where values are filled diagonally

        O(N^3). Apparently, my ability to decipher a diagonal DP has dropped.
        It is necessary to revisit the rod-cutting problem.

        8408 ms, also about 20x slower than the same solution submitted a year
        go. There is definitely change in the test case.
        """
        new_nums = [1] + [n for n in nums if n] + [1]  # always remove 0s first
        N = len(new_nums)
        dp = [[0] * N for _ in range(N)]

        for k in range(N - 2):  # the kth diagonal
            for j in range(k + 2, N):  # col index to indicate a diagonal cell
                i = j - 2 - k
                for l in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], new_nums[i] * new_nums[l] * new_nums[j] + dp[i][l] + dp[l][j])

        return dp[0][N - 1]


sol = Solution2()
tests = [
    ([3,1,5,8], 167),
    ([1,5], 10),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.maxCoins(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
