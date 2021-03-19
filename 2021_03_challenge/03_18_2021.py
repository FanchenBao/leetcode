# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """LeetCode 376

        DP solution. The (i + 1)th value is a tuple, with the first value
        being the index of the number that the ith number connects to in order
        to create the max wiggle sequence that ends at the ith number, and the
        second value being the length of the max wiggle sequence ending at the
        ith number. So we iterate through nums and update the DP array, when we
        finish, the answer is DP[N][1].

        For each DP action, we check the sign of the ith number and the (i - 1)th
        number, and the sign of the (i - 1)th number and the number right before
        the (i - 1)th number in the max wiggle sequence. If the two signs are
        not the same, we can add the ith number to the end of the wiggle sequence
        that ends at the (i - 1)th number. If the two signs are the same, then
        we add the ith number to the end of the max wiggle sequence that ends at
        the number right before the (i - 1)th number.

        If the ith and (i - 1)the numbers are the same, we simply copy the DP
        value of (i - 1)th number to ith number.

        The last tricky part is handling consecutive repeats at the beginning of
        the nums array. We must skip all of them to achieve a uniform solution.

        O(N), 36 ms, 62% ranking.
        """
        N = len(nums)
        dp = [None] * (N + 1)  # dp's index is 1-based
        j = 0  # Skip consecutive repeats from the beginning
        while j < N - 1 and nums[j] == nums[j + 1]:
            j += 1
        dp[j + 1] = (j + 1, 1)
        # Start dp at the first non-repeating number from the beginning
        for i in range(j + 1, N):  # nums's index is 0-based
            if nums[i] == nums[i - 1] or (nums[i] - nums[i - 1] > 0) is (nums[i - 1] - nums[dp[i][0]] > 0):
                dp[i + 1] = dp[i]
            else:
                dp[i + 1] = (i - 1, dp[i][1] + 1)
        return dp[N][1]


class Solution2:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """This is the up-down trend solution offered by the official solution.

        The idea is simple. Each number is either on an up or down trend. We use
        up and down to record the length of the max wiggle sequence that ends in
        an up or down trend. Thus, if a number is in an up trend, it can only
        be added to the most recent down trend; so we modify up by doing up =
        down + 1. Similarly, if a number is in a down trend, it can only be
        added to the most recent up trend; so we do down = up + 1. If the number
        is the same as the previous, we do not change up or down.

        O(1) space and O(N) time.
        """
        up, down = 1, 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 0:
                up = down + 1
            elif nums[i] - nums[i - 1] < 0:
                down = up + 1
        return max(up, down)


sol = Solution2()
tests = [
    ([1, 7, 4, 9, 2, 5], 6),
    ([1, 17, 5, 10, 13, 15, 10, 5, 16, 8], 7),
    ([1, 2, 3, 4, 5, 6], 2),
    ([1, 4, 7, 2, 5], 4),
    ([1, 7, 4, 5, 5], 4),
    ([1, 1, 1, 1], 1),
    ([1], 1),
    ([1, 2], 2),
    ([2, 1], 2),
    ([1, 1, 1, 1, 3], 2),
    ([2, 2, 1, 1, 3, 3], 3),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.wiggleMaxLength(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
