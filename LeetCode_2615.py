# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict
from itertools import accumulate


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        """Find the groups of indices that belong together, make sure they are
        sorted, then use prefix sum to quickly compute the sum of distances.

        O(N), 781 ms, faster than 98.06%
        """
        indices = defaultdict(list)
        for i, n in enumerate(nums):
            indices[n].append(i)
        res = [0] * len(nums)
        for vals in indices.values():
            if len(vals) > 1:
                psum = list(accumulate(vals, initial=0))
                for i, v in enumerate(vals):
                    res[v] = i * v - psum[i] + (psum[-1] - psum[i + 1]) - (len(vals) - 1 - i) * v
        return res
        

sol = Solution()
tests = [
    ([1,3,1,1,2], [5,0,3,4,0]),
    ([0,5,3], [0,0,0]),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.distance(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
