# from pudb import set_trace; set_trace()
from typing import List
import math
from random import randint


class Solution0:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """TLE, because if every value in nums is positive, it runs in O(N^2)
        """
        N = len(nums)
        dup_nums = nums + nums
        res = -math.inf
        cur = c = 0  # c is count, cur is current max
        for i, n in enumerate(dup_nums):
            if c == N:
                # subarray full. we need to remove from the head and obtain the
                # largest subarray sum ending at nums[i - 1].
                tmp = -math.inf
                for j in range(i - N, i):
                    cur -= dup_nums[j]
                    if cur >= tmp:
                        tmp = cur
                        c = i - j - 1
                cur = tmp
            if n >= cur + n:
                cur = n
                c = 1
            else:
                cur += n
                c += 1
            res = max(res, cur)
        return res


class Solution1:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """LeetCode 918

        So bad. So bad. End up with a hacking solution. I am sure the actual
        solution is not like this at all!

        Will read the solution tomorrow.

        O(N^2), 3930 ms, faster than 5.07%
        """
        N = len(nums)
        dup_nums = nums + nums
        res = -math.inf
        cur = c = 0  # c is count, cur is current max
        cn = 0  # number of non-positive values
        for i, n in enumerate(dup_nums):
            if c == N:
                # remove from the head until all negative values are exhausted
                # keep track of when the largest sum ending at nums[i - 1] is
                # reached.
                cur -= dup_nums[i - c]
                cn -= int(dup_nums[i - c] <= 0)
                c -= 1
                tmp_cur, tmp_c, tmp_cn = cur, c, cn
                while cn:
                    cur -= dup_nums[i - c]
                    cn -= int(dup_nums[i - c] <= 0)
                    c -= 1
                    if cur >= tmp_cur:
                        tmp_cur = cur
                        tmp_c = c
                        tmp_cn = cn
                cur, c, cn = tmp_cur, tmp_c, tmp_cn
            if n >= cur + n:
                cur = n
                c = 1
                cn = int(n <= 0)
            else:
                cur += n
                c += 1
                cn += int(n <= 0)
            res = max(res, cur)
        return res


sol0 = Solution0()
sol = Solution1()

tests = [[randint(-10, 10) for _ in range(10)] for _ in range(10000)]

for i, nums in enumerate(tests):
    ans = sol0.maxSubarraySumCircular(nums)
    res = sol.maxSubarraySumCircular(nums)
    if res != ans:
        print(f'Test: {nums} ; Fail. Ans: {ans}, Res: {res}')

# tests = [
#     ([1,-2,3,-2], 3),
#     ([5,-3,5], 10),
#     ([-3,-2,-3], -2),
#     ([-1, 9, -4, 3, 7], 18),
#     ([10, 2, -7, 7, -4], 15),
#     ([7, 7, -6, -4, 3], 17),
#     ([10, -7, 1, -3, 6], 16),
#     ([8, 6, -3, 2, -5, 7], 21),
#     ([9, 10, -8, 7, -8, 10], 29),
# ]

# for i, (nums, ans) in enumerate(tests):
#     res = sol.maxSubarraySumCircular(nums)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
