# from pudb import set_trace; set_trace()
from typing import List
from itertools import accumulate
import operator
from bisect import bisect_right
import math


class Solution1:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """One pass is required, otherwise TLE

        This solution has very good performance. It multiplies consecutive
        numbers from the start. If, at ith position, the cumulative product
        exceeds k, it counts the number of consecutive subarray from start to
        i - 1 position that includes the starting number. This count is saved
        to the result. We then remove the starting number from the cumulative
        product. This process repeats until the product is smaller than k, and
        we proceeds to check the i + 1 position. When all checks are done, we
        are left with a subarray of numbers whose cumulative product is smaller
        than k. All consecutive subarrays in this sfinal subarray can be
        counted towards the result. Finally, the result is returned.
        """
        res = 0
        prod, s = 1, 0
        for i, n in enumerate(nums):
            prod *= n
            while prod >= k and s <= i:
                res += i - s
                prod //= nums[s]
                s += 1
        return res + (i - s + 1) * (i - s + 2) // 2


class Solution2:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """Official slide window solution. The anchor is on the right side,
        instead of the left side as in Solution1. This version is much easier
        to reason with.
        """
        if k == 0:
            return 0
        res, prod, left = 0, 1, 0
        for right, n in enumerate(nums):
            prod *= n
            while prod >= k and left <= right:
                prod //= nums[left]
                left += 1
            res += right - left + 1
        return res


class Solution3:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """Using binary search, but this one TLE, most likely due to too
        many multiplication.
        """
        acc = list(accumulate(nums, operator.mul))
        res = 0
        for i in range(len(acc)):
            pre = acc[i - 1] if i > 0 else 1
            pos = bisect_right(acc, pre * k - 1) - 1
            res += pos - i + 1 if pos >= i else 0
        return res


class Solution4:
    def numSubarrayProductLessThanK(self, nums, k):
        """Same binary search method as Solution3, but this one passed OJ,
        most likely because addition is faster than multiplication.
        """
        if k == 0: 
            return 0
        k = math.log(k)
        acc = list(accumulate([math.log(n) for n in nums], operator.add))
        res = 0
        for left in range(len(acc)):
            pre = acc[left - 1] if left > 0 else 0
            right = bisect_right(acc, pre + k - 1e-5) - 1
            res += right - left + 1 if right >= left else 0
        return res




sol = Solution4()
tests = [
    ([10, 5, 2, 6], 100, 8),
    ([1, 2, 3], 0, 0),
    ([1, 1, 1], 1, 0),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.numSubarrayProductLessThanK(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
