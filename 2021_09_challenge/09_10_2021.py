# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter, defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """LeetCode 446

        I failed. But I am close. I was thinking about the length of a sub-
        sequence ending at a specific value in nums. But the correct answer is
        the total number of weak subsequences (i.e. subsequence including length
        of 2) ending at a specific value. By doing so, we avoid the complexity
        of using an array to keep track of all different lenghts, and also
        avoid duplicating the results.

        We already know the trick, that when we are at a new value, any previous
        value can form a 2-size weak subsequence with the current value. That is
        the only trick in this problem, aside from using the number of
        subsequences as the DP target. We also figure out ourselves that one of
        the DP dimension has to be difference.

        O(N^2)
        """
        N = len(nums)
        memo = [defaultdict(int) for _ in range(N)]
        res = 0
        for i in range(1, N):
            for j in range(i):
                diff = nums[i] - nums[j]
                res += memo[j][diff]  # avoid including weak subsequence
                memo[i][diff] += memo[j][diff] + 1
        return res


sol = Solution()
tests = [
    ([2, 4, 6, 8, 10], 7),
    ([7, 7, 7, 7, 7], 16),
    ([2, 4, 6, 8, 10, 6, 8], 12),
    ([1, 1, 2, 3, 4], 5),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.numberOfArithmeticSlices(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
