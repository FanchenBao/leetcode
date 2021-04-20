# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache


class Solution1:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """377

        TLE!!
        """
        res = []
        N = len(nums)

        def helper(cur: List, cur_target: int) -> None:
            if cur_target == 0:
                res.append(cur[:])
            elif cur_target > 0:
                for i in range(N):
                    cur.append(nums[i])
                    helper(cur, cur_target - nums[i])
                    cur.pop()

        helper([], target)
        return len(res)


class Solution2:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """Wasn't able to solve this one by myself. Had to refer to the solution
        here:

        https://leetcode.com/problems/combination-sum-iv/discuss/85036/1ms-Java-DP-Solution-with-Detailed-Explanation

        Why did we get stuck initially? We were stuck on how to actually do
        permutation with no repeats. But in fact, we don't have to do that,
        because if we fix the first position as a different value, we don't have
        to worry about repetition at all.

        Basically, we are saying, given the problem [1, 2, 3] => 4, let the
        first position be 1, then we want to find all possible unique
        permutations that allows [1, 2, 3] => 3. Then we fix the first position
        to be 2, then we want to final all possible unique permutations that
        allows [1, 2, 3] => 2. We don't have to worry about repeats between
        these two operations, because the first one always starts with 1, while
        the second 2.

        Hence the memoization recursion solution.
        """

        @lru_cache(maxsize=None)
        def helper(cur_target: int) -> int:
            if cur_target == 0:
                return 1
            res = 0
            for n in nums:
                if n <= cur_target:
                    res += helper(cur_target - n)
            return res

        return helper(target)


class Solution3:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """Bottom up DP.

        O(TN), where T = target and N = len(nums)
        """
        dp = [0] * (target + 1)
        dp[0] = 1
        for t in range(1, target + 1):
            for n in nums:
                if t - n >= 0:
                    dp[t] += dp[t - n]
        return dp[target]


sol = Solution3()
tests = [
    ([1, 2, 3], 4, 7),
    ([9], 3, 0),
    ([1, 2, 4], 8, 55),
    ([4, 2, 1], 32, 39882198),
]

for i, (nums, target, ans) in enumerate(tests):
    res = sol.combinationSum4(nums, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
