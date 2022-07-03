# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """LeetCode 376
        
        Very naive DP solution. For each new n, we go through all the previous
        numbers and check whether we can make a longer subsequence.

        O(N^2), 220 ms, faster than 17.85% 
        """
        N = len(nums)
        dp = [[1, 1] for _ in range(N)]
        res = 1
        for i in range(1, N):
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j]:
                    dp[i][0] = max(dp[i][0], dp[j][1] + 1)
                elif nums[i] < nums[j]:
                    dp[i][1] = max(dp[i][1], dp[j][0] + 1)
            res = max(res, *dp[i])
        return res


class Solution2:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """This is from the official solution.

        We use an up and down arrays. up[i] is the length of the longest wiggle
        sequence from 0 to i that ends in an up trend. down[i] is the length of
        the longest wiggle sequence that ends in a down trend.

        O(N), 40 ms, faster than 84.95%

        UPDATE: array is not necessary, because we only access the previous
        value in up or down. So we can do it in O(1) space.
        """
        N = len(nums)
        up, down = 1, 1
        for i in range(1, N):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1
        return max(up, down)


sol = Solution2()
tests = [
    ([1,7,4,9,2,5], 6),
    ([1,17,5,10,13,15,10,5,16,8], 7),
    ([1,2,3,4,5,6,7,8,9], 2),
    ([1], 1),
    ([1, 2], 2),
    ([1, 1], 1),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.wiggleMaxLength(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
