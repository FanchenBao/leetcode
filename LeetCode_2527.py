# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        """Notice that

        1. When i != j, (i | j) & k == (j | i) & k
        2. When i == j but != k, (i | i) & k == (k | k) & i

        Thus all i, j, k triplets can find its corresponding pair that would
        yield the same value. And XOR two same values lead to 0. The only i, j,
        k that will not be canceled by XOR is when i == j == k. Hence the answer
        is to XOR everything in nums

        O(N), 354 ms, faster than 81.25%
        """
        res = 0
        for n in nums:
            res ^= n
        return res


sol = Solution()
tests = [
    ([1,4], 5),
    ([15,45,20,2,34,35,5,44,32,30], 34),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.xorBeauty(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
