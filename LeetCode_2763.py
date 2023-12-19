# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        """
        Create a state for the values in nums, where state[nums[i]] represents
        whether nums[i] has been encountered.

        We go through all subarrays in nums (we can do so because the size of
        nums is at most 1000).

        For each subarray, we keep track of the imbalance number so far. For
        a new number encountered, if this number has been seen before, including
        it in the new subarray does not alter the imbalance number. If the new
        number is placed in such a way that its neighbors have not been seen
        before, then the new number creates an additional imbalance number.

        If the new number's neighbors have already been seen before, then the
        new number reduces one count of imbalance number.

        if the new number only has one of its neighbor seen before, it does not
        change the count of imbalance number.

        We create such state for each series of subarrays starting from nums[i]
        and accumulate all the imbalance numbers.

        O(N^2) 381 ms, faster than 48.28%
        """
        res = 0
        N = len(nums)
        for i in range(N):
            state = [False] * (N + 1)
            state[nums[i]] = True
            cur = 0
            for j in range(i + 1, N):
                k = nums[j]
                if not state[k] and not state[k - 1] and (k == N or not state[k + 1]):
                    cur += 1
                elif not state[k] and state[k - 1] and (k < N and state[k + 1]):
                    cur -= 1
                res += cur
                state[k] = True
        return res


sol = Solution()
tests = [
    ([2,3,1,4], 3),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.sumImbalanceNumbers(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
