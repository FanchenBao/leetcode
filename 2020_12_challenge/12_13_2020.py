# from pudb import set_trace; set_trace()
from typing import List, Tuple
from functools import lru_cache


class Solution1:
    @lru_cache(maxsize=None)
    def helper(self, nums: Tuple) -> int:
        max_coins = 0
        for i, n in enumerate(nums[1:-1], 1):
            max_coins = max(
                max_coins, 
                n * nums[i - 1] * nums[i + 1] + self.helper(nums[:i] + nums[i + 1:]),
            )
        return max_coins

    def maxCoins(self, nums: List[int]) -> int:
        """TLE. This is a very naive approach, so TLE is not unexpected."""
        return self.helper(tuple([1] + nums + [1]))


class Solution2:

    def maxCoins(self, nums: List[int]) -> int:
        """This is a hard problem. And indeed it surely is. I couldn't figure
        it out, so I refer to the solution. This is a typical DP problem, on
        the same level as the matrix multiplication and rod cutting. The trick
        is with how to divide the problems into subproblems.

        I was thinking about dividing the ballons into two, take the max on
        each, and then figure out a way to consider the situation where the
        spanning balloons get burst. However, this is too complicated, and I
        discarded the idea.

        The solution chooses the LAST balloon to burst as the dividing point.
        The benefit of using the last balloon is that the two subproblems on
        the left and right do not cross over the last burst balloon. In other
        words, we have two independent subproblems. And this is the chance for
        DP.

        Actually, in the question, the hint is already there. The question
        says to consider nums[-1] = nums[n] = 1, which kind of hints that we
        should use boundary indices. During the divide and conquer, we do need
        to use the boundary indices, because when the last burst is selected,
        it becomes the right boundary of the left subproblem, and the left
        boundary of the right subproblem.

        Another important part of this solution is to use the appropriate
        vairables for the memo. I was just throwinig lru_cache with no
        consideration of what actually should be cached. The answer is the
        boundaries. In my previus attempt, I was actively recreating new nums
        for each recursion, and I was hoping that there could be repeats of the
        actual nums array (i have to turn them into tuple for use in lru_cache)
        Now that is not the right way to go, because the chance of the content
        of the nums array to match during recursion is quite low, so the
        lru_cache cannot exert its power. The correct way is to not recreate
        any new arrays, but use the left and right boundary indices as the
        target for cache.

        The solution below is almost exactly the same as the one provided in
        this post:

        https://leetcode.com/problems/burst-balloons/discuss/76228/Share-some-analysis-and-explanations

        O(N^3), 712 ms, 18% ranking.
        """
        new_nums = [1] + [n for n in nums if n > 0] + [1]
        n = len(new_nums)
        memo = [[0] * n for _ in range(n)]

        def helper(li: int, ri: int) -> int:
            if li + 1 == ri:  # no number within boundary
                return 0
            if memo[li][ri] > 0:
                return memo[li][ri]
            max_coins = 0
            for i in range(li + 1, ri):
                max_coins = max(
                    max_coins,
                    new_nums[li] * new_nums[i] * new_nums[ri] + helper(li, i) + helper(i, ri)
                )
            memo[li][ri] = max_coins
            return max_coins

        return helper(0, n - 1)


class Solution3:

    def maxCoins(self, nums: List[int]) -> int:
        """This is the bottom up solution. Although I wasn't able to figure out
        the initial solution, at least I was able to convert the top down to
        the bottom up solution.

        We fill out the memo matrix diagonally. `k` is the number of diagonals
        we need to fill. i and j are the boundary indices.

        O(N^3), 404 ms, 79% ranking.
        """
        nums = [1] + [n for n in nums if n > 0] + [1]
        n = len(nums)
        memo = [[0] * n for _ in range(n)]
        for k in range(n - 2):
            for j in range(k + 2, n):
                i = j - k - 2
                for idx in range(i + 1, j):
                    memo[i][j] = max(memo[i][j], nums[idx] * nums[i] * nums[j] + memo[i][idx] + memo[idx][j])
        return memo[0][n - 1]


sol = Solution3()
tests = [
    ([3, 1], 6),
    ([3, 1, 5], 35),
    ([3, 1, 5, 8], 167),
    ([1, 2], 4),
    ([1], 1),
    ([], 0),
    ([3, 0, 5], 20),
    ([8, 3, 4, 3, 5, 0], 364),
    ([1, 2, 3, 4, 5], 110),
    ([85, 1, 83, 88, 27, 74, 68, 100, 71, 29, 7, 76, 53, 45, 62, 33, 67, 30, 27, 83, 48, 53, 28, 52, 21, 46, 0, 83, 12, 0, 79, 61, 12, 59, 9, 70, 47, 34, 64, 80, 38, 77, 79, 53, 65, 34, 28, 55, 48, 33, 12, 19, 26, 62, 90, 14, 21, 8, 55, 82, 40, 5, 29, 56, 73, 13, 51, 20, 21, 61, 26, 73, 69, 89, 87, 93, 42, 34, 18, 88, 53, 98, 6, 53, 13, 78, 68, 7, 34, 0, 5, 7, 82, 85, 5, 6, 50, 94, 69, 88, 35, 24, 85, 38, 21, 50, 64, 25, 48, 46, 83, 85, 37, 88, 12, 63, 29, 59, 5, 37, 67, 44, 58, 5, 93, 56, 91, 42, 71, 61, 85, 88, 2, 91, 99, 72, 31, 16, 19, 63, 62, 47, 80, 14, 54, 97, 92, 17, 43, 52, 68, 15, 53, 36, 44, 95, 26, 9, 92, 41, 89, 70, 45, 35, 6, 95, 100, 51, 47, 62, 51, 90, 89, 50, 66, 92, 56, 20, 85, 56, 38, 8, 95, 3, 62, 94, 46, 23, 41, 63, 67, 18, 34, 54, 0, 53, 100, 61, 47, 62, 12, 87, 40, 69, 32, 79, 29, 88, 80, 34, 57, 53, 35, 35, 24, 95, 0, 9, 59, 40, 88, 31, 89, 98, 19, 1, 44, 41, 69, 46, 46, 43, 69, 37, 9, 16, 19, 34, 15, 9, 39, 7, 51, 5, 94, 93, 58, 43, 83, 13, 68, 91, 24, 18, 19, 53, 11, 94, 5, 0, 7, 76, 65, 95, 53, 15, 93, 6, 77, 47, 55, 77, 22, 15, 34, 2, 74, 6, 69, 32, 1, 70, 42, 63, 13, 72, 89, 74, 12, 46, 67, 24, 49, 83, 41, 85, 11, 29, 87, 43, 13, 9, 8, 23, 18, 28, 63, 66, 23, 25, 38, 84, 76, 4, 64, 93, 41, 11, 61, 22, 56, 39, 84, 93, 65, 80, 46, 26, 66, 12, 39, 68, 31, 44, 93, 86, 65, 24, 29, 43, 12, 53, 60, 34, 84, 57, 57, 100, 55, 36, 11, 91, 7, 69, 43, 51, 87, 92, 25, 35, 65, 27, 89, 71, 50, 3, 91, 86, 94, 4, 94, 27, 0, 30, 38, 76, 75, 12, 23, 52, 41, 33, 87, 22, 21, 88, 4, 4, 44, 16, 73, 34, 42, 85, 38, 96, 58, 79, 3, 100, 56, 99, 29, 77, 77, 5, 73, 29, 94, 41, 99, 29, 2, 8, 52, 25, 3, 37, 43, 53, 82, 19, 63, 11, 84, 21, 89, 9, 56, 13, 6, 74, 75, 30, 24, 14, 2, 40, 42, 91, 20, 8, 14, 63, 35, 43, 65, 76, 40, 50, 7, 17, 86, 49, 93, 41, 95, 30, 94, 72, 69, 12, 83, 50, 19, 33, 24, 7, 34, 22, 72, 22, 55, 71, 3, 99, 23, 49, 24, 77, 18, 22, 74, 58, 35, 21, 6, 18, 9, 6, 79, 37, 10, 23, 73, 49, 63, 71, 95, 96], 170898328)
]

for i, (nums, ans) in enumerate(tests):
    res = sol.maxCoins(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
