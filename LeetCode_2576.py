# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter
from bisect import bisect_left


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        counter = Counter(nums)
        keys = sorted(counter)
        res = 0
        i = 0
        j = bisect_left(keys, keys[0] * 2)
        M = len(keys)
        print(counter, keys)
        while j < M:
            while i < M and counter[keys[i]] == 0:
                i += 1
            while j < M and (keys[i] * 2 > keys[j] or counter[keys[j]] == 0):
                j += 1
            while j < M and counter[keys[j]] <= counter[keys[i]]:
                counter[keys[i]] -= counter[keys[j]]
                res += 2 * counter[keys[j]]
                counter[keys[j]] = 0
                j += 1
            if j < M:
                counter[keys[j]] -= counter[keys[i]]
                res += 2 * counter[keys[i]]
                counter[keys[i]] = 0
                i += 1
        return res


sol = Solution()
tests = [
    # ([3,5,2,4], 2),
    ([9,2,5,4], 4),
    # ([7,6,8], 0),
    # ([67,56,456,56,567,67,678,42,5654,345,342,345,45,456,3], 14),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.maxNumOfMarkedIndices(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
