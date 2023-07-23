# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        """
        """
        N = len(nums)
        sufor = [0] * N
        sufor[-1] = nums[-1]
        for i in range(N - 2, -1, -1):
            sufor[i] = sufor[i + 1] | nums[i]

        @lru_cache(maxsize=None)
        def dp(idx: int, rem: int) -> int:
            if idx == N:
                return 0
            if rem == 0:
                return sufor[idx]
            res = 0
            for i in range(rem + 1):
                res = max(res, (nums[idx] * (1 << i)) | dp(idx + 1, rem - i))
            # print(idx, rem, res)
            return res

        return dp(0, k)
        

sol = Solution()
tests = [
    ([12,9], 1, 30),
    ([8,1,2], 2, 35),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.maximumOr(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
