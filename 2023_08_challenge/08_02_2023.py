# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """LeetCode 46

        41 ms, faster than 97.30%
        """
        N = len(nums)
        
        def helper(idx: int) -> List[List[int]]:
            if idx == N - 1:
                return [[nums[idx]]]
            res = []
            for perm in helper(idx + 1):
                for i in range(len(perm) + 1):
                    res.append(perm[:i] + [nums[idx]] + perm[i:])
            return res

        return helper(0)

sol = Solution()
tests = [
    ([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
    ([0,1], [[0,1],[1,0]]),
    ([1], [[1]]),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.permute(nums)
    if sorted(res) == sorted(ans):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
