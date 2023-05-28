# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_left
from itertools import accumulate
from collections import defaultdict


class Solution1:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        """Solid analysis. Sort nums. Binary search q inside nums to decide
        how many values are smaller and how many bigger than q. Use prefix sum
        to quickly obtain the sum of the smaller and sum of the bigger. The
        answer for the current query is q times the number of smaller minus the
        sum of the smaller plus the sum of the bigger minus q times the number
        of bigger.

        The complications are:

        1. q might be equal to a value in nums.
        2. The value in nums that is equal to q might have duplications.

        O(NlogN), 1011 ms, faster than 58.90%
        """
        nums.sort()
        N = len(nums)
        presum = list(accumulate(nums))
        indices = defaultdict(int)
        for i, n in enumerate(nums):
            indices[n] = i
        res = []
        for q in queries:
            idx = bisect_left(nums, q)
            small = presum[idx - 1] * int(idx > 0)
            if idx == N:
                res.append(q * N - presum[-1])
            elif nums[idx] != q:
                big = presum[-1] - presum[idx - 1] * int(idx > 0)
                res.append(q * idx - small + big - q * (N - idx))
            else:
                big = presum[-1] - presum[indices[q]]
                res.append(q * idx - small + big - q * (N - indices[q] - 1))
        return res


class Solution2:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        """No need to analyze the complications, because any repeated values in
        nums that are equal to q will be canceled when we do big - q * num_big.

        Dumb me!! O(NlogN) 941 ms, faster than 93.34%
        """
        nums.sort()
        N = len(nums)
        presum = [0] + list(accumulate(nums))
        res = []
        for q in queries:
            idx = bisect_left(nums, q)
            small = presum[idx]
            big = presum[-1] - presum[idx]
            res.append(q * idx - small + big - q * (N - idx))
        return res

        

sol = Solution2()
tests = [
    ([3,1,6,8], [1,5], [14, 10]),
    ([2,9,6,3], [10], [20]),
]

for i, (nums, queries, ans) in enumerate(tests):
    res = sol.minOperations(nums, queries)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
