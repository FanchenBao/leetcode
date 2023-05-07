# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        """LeetCode 1498

        Since it is subsequence, we can sort nums. Then for each value from left
        to right, we can find all the subsequences that starts from that value.

        Since that value is the min, we just need to use target - min to find
        the max allowed value. Then we search in nums to locate where is the
        max value that is smaller than the max allowed. Then all the numbers in
        between the max value and min value can be attached to the min value.

        We can use binary search to locate the max value that is smaller than
        the max allowed. But, a two-pointer method is more efficient.

        Furthermore, the count of available subsequences is power of two. Since
        the power can be huge, we need to use the pow() function to MOD while
        performing the power.

        O(NlogN), 800 ms, faster than 89.64%
        """
        nums.sort()
        j = len(nums) - 1
        res = 0
        MOD = 10**9 + 7
        for i, n in enumerate(nums):
            while i <= j and nums[j] > target - n:
                j -= 1
            if i > j:
                break
            res += pow(2, j - i, MOD)
        return res % MOD
        

sol = Solution()
tests = [
    ([3,5,6,7], 9, 4),
    ([3,3,6,8], 10, 6),
    ([2,3,3,4,6,7], 12, 61),
]

for i, (nums, target, ans) in enumerate(tests):
    res = sol.numSubseq(nums, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
