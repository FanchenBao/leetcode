# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution1:
    def longestConsecutive(self, nums: List[int]) -> int:
        """LeetCode 128

        Start from any number, and increment. We try to make as much increment
        as possible, and each time we check whether the incremented value is in
        the original array. One trick is that if a value has been checked
        before, we can use its value to jump forward. Hence, we need another
        Counter to perform as a dp table.

        O(N), 746 ms, faster than 44.57%
        """
        if not nums:
            return 0
        num_counter = Counter(nums)
        dp = Counter()
        for n in num_counter:
            tmp = n
            size = 0
            while num_counter[tmp]:
                num_counter[tmp] -= 1
                inc = max(1, dp[tmp])
                size += inc
                tmp += inc
            dp[n] = size + dp[tmp]
        return max(dp.values())


class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        """Solution1 is not the best. This is from more than a year ago, and it
        directly turns nums into a set. We go through nums, and if we hit a
        value that is supposed to be in the longest continuous sequence, we go
        higher and lower, and that shall hit everything. And we are done.

        O(N), 615 ms, faster than 52.11%
        """
        num_set = set(nums)
        res = 0
        for n in nums:
            x = n + 1  # go higher
            while x in num_set:
                num_set.remove(x)
                x += 1
            x -= 1
            y = n - 1 # go lower
            while y in num_set:
                num_set.remove(y)
                y -= 1
            y += 1
            res = max(res, x - y + 1)
        return res


sol = Solution2()
tests = [
    ([], 0),
    ([100,4,200,1,3,2], 4),
    ([0,3,7,2,5,8,4,6,0,1], 9),
    ([1,2,0,1], 3),
    ([-2,-3,-3,7,-3,0,5,0,-8,-4,-1,2], 5),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.longestConsecutive(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
