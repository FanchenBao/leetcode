# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        """For each query, check its left and right, and decide whether we need
        to update the total count of pairs of adjacent values.

        O(N), 2519 ms, faster than 63.97%
        """
        res = [0]
        nums = [0] * n
        nums[queries[0][0]] = queries[0][1]
        for idx, c in queries[1:]:
            res.append(res[-1])
            if idx - 1 >= 0:
                if nums[idx] == nums[idx - 1] and nums[idx]:
                    res[-1] -= 1
                if c == nums[idx - 1]:
                    res[-1] += 1
            if idx + 1 < n:
                if nums[idx] == nums[idx + 1] and nums[idx]:
                    res[-1] -= 1
                if c == nums[idx + 1]:
                    res[-1] += 1
            nums[idx] = c
        return res


sol = Solution()
tests = [
    (4, [[0,2],[1,2],[3,1],[1,1],[2,1]], [0,1,1,0,2]),
    (1, [[0,100000]], [0])
]

for i, (n, queries, ans) in enumerate(tests):
    res = sol.colorTheArray(n, queries)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
