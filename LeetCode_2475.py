# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter
from itertools import accumulate


class Solution1:
    def unequalTriplets(self, nums: List[int]) -> int:
        """Dumbest method

        O(N^3), 3370 ms, faster than 6.58%
        """
        N = len(nums)
        res = 0
        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    res += int((nums[i] - nums[j]) * (nums[j] - nums[k]) * (nums[i] - nums[k]) != 0)
        return res


class Solution2:
    def unequalTriplets(self, nums: List[int]) -> int:
        """Basically the problem can be converted to given an array of numbers
        a, b, c, d, ..., compute the sum of the product of all combinations of
        three, such as: abc + abc + acd + bcd + ...

        This array is the values of Counter(nums). And to make the computation
        faster, we use prefix sum on the array and run O(N^2) on the first two
        values.

        160 ms, faster than 89.77%
        """
        c = Counter(nums)
        if len(c) < 3:
            return 0
        presum = list(accumulate(c.values(), initial=0))
        res = 0
        for i in range(1, len(presum)):
            for j in range(i + 1, len(presum)):
                res += (presum[i] - presum[i - 1]) * (presum[j] - presum[j - 1]) * (presum[-1] - presum[j])
        return res


class Solution3:
    def unequalTriplets(self, nums: List[int]) -> int:
        """Even better. This can be done in O(N)

        Inspired by: https://leetcode.com/problems/number-of-unequal-triplets-in-array/discuss/2831702/O(n)

        Still, take the same array idea as in Solution2, but we focus on the
        middle number.

        array = [a, b, c, d, e, f, g]

        If the triplet has d in the middle. We have

        res = cd(e + f + g) + bd(e + f + g) + ad(e + f + g)
        = (a + b + c)d(e + f + g)

        The sum on both sides can be computed via presum.

        O(N), 45 ms, faster than 97.99%
        """
        presum = list(accumulate(Counter(nums).values(), initial=0))
        return sum(presum[i - 1] * (presum[i] - presum[i - 1]) * (presum[-1] - presum[i]) for i in range(1, len(presum)))






# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
