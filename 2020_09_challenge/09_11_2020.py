# from pudb import set_trace; set_trace()
from typing import List
from functools import reduce
from itertools import accumulate
import operator


class Solution1:
    def helper(self, idx: int, nums: List) -> int:
        res, curr_max = nums[idx], 1
        for i in range(idx, len(nums)):
            curr_max = curr_max * nums[i] if abs(curr_max * nums[i]) >= nums[i] else nums[i]
            res = max(res, curr_max)
        return res

    def maxProduct(self, nums: List[int]) -> int:
        """TLE"""
        prod = reduce(lambda x, y: x * y, nums)
        if prod > 0:
            return prod


class Solution2:
    def helper(self, start: int, end: int, cum_prod: List[int]) -> int:
        if cum_prod[end] > 0:
            return cum_prod[end]
        if start >= end:
            return cum_prod[start]
        res = cum_prod[end] // cum_prod[start]
        for i in range(start + 1, end + 1):
            res = max([res, cum_prod[i - 1], cum_prod[end] // cum_prod[i]])
        return res

    def maxProduct(self, nums: List[int]) -> int:
        """Pass the OJ with 48 ms runtime. It is at 97%, but honestly this
        is one of the worst Frankenstein algorithm I have written. Totally
        disgusted by it.
        """
        zero_pos = [i for i, n in enumerate(nums) if n == 0]
        cum_prod = [nums[0]]
        for n in nums[1:]:
            if n == 0:
                cum_prod.append(n)
            elif cum_prod[-1] == 0:
                cum_prod.append(n)
            else:
                cum_prod.append(cum_prod[-1] * n)
        if zero_pos:
            res, start = 0, 0
            for zero_idx in zero_pos:
                res = max(res, self.helper(start, zero_idx - 1, cum_prod))
                start = zero_idx + 1
            if start < len(nums):
                res = max(res, self.helper(start, len(nums) - 1, cum_prod))
            return res
        else:
            return self.helper(0, len(nums) - 1, cum_prod)


class Solution3:
    def maxProduct(self, A):
        """This is the black magic solution
        https://leetcode.com/problems/maximum-product-subarray/discuss/183483/Easy-and-Concise-Python

        I actually almost got here from Solution2. I understand that to find the
        max, we need to check the cum_prod[i - 1], cum_prod[end] // cum_prod[i].
        These two represent exactly the prefix prod and suffix prod. So I am
        already doing the comparison of all prefix prods and suffix prods, yet
        to get from Solution2 to Solution3, the gap is enourmous.
        """
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(A + B)


class Solution4:
    def maxProduct(self, nums: List[int]):
        """This is based on Kadane's algorithm."""
        cur_min, cur_max, res = nums[0], nums[0], nums[0]
        for n in nums[1:]:
            temp_min = cur_min * n  # temp_min could be neg, 0, or pos
            temp_max = cur_max * n  # temp_max could be neg, 0, or pos
            cur_min = min(temp_min, n, temp_max)  # true cur_min
            cur_max = max(temp_min, n, temp_max)  # true cur_max
            res = max(cur_max, res)
        return res



sol = Solution4()
tests = [
    ([2, 3, -2, 4], 6),
    ([-2, 0, -1], 0),
    ([-2, 0, 1, -1], 1),
    ([1, 2, 0, 2, 3, 0, 1, 1], 6),
    ([2, 3, -2, 4, -4, 5, -6, 7, 8, -1, -1, -4, 4, 5], 25804800),
    ([2, 3, -2, 4, -4, 5, 6, 7, 8, -1, -1, -4, 4, 5], 2150400),
    ([2, 3, -2], 6),
    ([2, 3, -2, 4], 6),
    ([2, 3, -2, 4, -4], 192),
    ([2, 3, -2, 4, -4, 5, 6, 7, 8, -1], 322560),
    ([2, 3, -2, 4, -4, -4, 10, 3], 1920),
    ([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2], 2),
    ([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2], 2),
    ([-1, 2, 2, -3], 12),
    ([0], 0),
    ([1, 0, -1, 2, 3, -5, -2], 60),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.maxProduct(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
