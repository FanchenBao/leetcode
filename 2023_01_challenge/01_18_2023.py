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


class Solution2:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """Official solution, use prefix and suffix sum to find the max sum of
        a crossing array that does not overlap.

        dp[i] records the max suffix sum starting at i or later.

        O(N), 624 ms, faster than 50.29%
        """
        N = len(nums)
        # build dp
        dp = [0] * N
        dp[-1] = nums[-1]
        suf_sum = nums[-1]
        for i in range(N - 2, -1, -1):
            suf_sum += nums[i]
            dp[i] = max(dp[i + 1], suf_sum)
        # find max crossing sum
        max_cross = -math.inf
        pre_sum = 0
        for i in range(N - 1):
            pre_sum += nums[i]
            max_cross = max(max_cross, pre_sum + dp[i + 1])
        # use Kadane to find normal max subarray sum
        kadane = -math.inf
        cur_max = -math.inf
        for n in nums:
            cur_max = max(n, cur_max + n)
            kadane = max(kadane, cur_max)
        return max(kadane, max_cross)


class Solution3:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """Another solution from the official solution. Instead of finding the
        max sum of a prefix and suffix sum, we find a min subarray sum in nums.
        Then the remaining must be the max cross sum. This min subarray sum can
        be found using Kadane. Pay attention to the edge case where all nums are
        negative, in which canse the min subarray sum would be the entire array.
        That would lead to the max cross sum being zero. But in this case, the
        answer should be a negative value. We need to check whether all numbers
        are negative.

        Lord this is brilliant!

        O(N), 583 ms, faster than 59.70%

        UPDATE: no need to count negative. If max_cross is zero, we will always
        use Kadane. Because if max_cross is zero due to all numbers being neg,
        we shall use Kadane. If max_cross is zero not because all numbers being
        neg, then zero is indeed the max_cross. But that also means there must
        exist some non-neg values which can be picked up by Kadane.

        521 ms, faster than 91.82%
        """
        min_subsum = cur_min = math.inf
        max_subsum = cur_max = -math.inf
        for n in nums:
            cur_min = min(n, cur_min + n)
            min_subsum = min(min_subsum, cur_min)
            cur_max = max(n, cur_max + n)
            max_subsum = max(max_subsum, cur_max)
        total = sum(nums)
        return max_subsum if total == min_subsum else max(max_subsum, total - min_subsum)




sol0 = Solution0()
sol = Solution3()

# tests = [[randint(-10, 10) for _ in range(10)] for _ in range(10000)]

# for i, nums in enumerate(tests):
#     ans = sol0.maxSubarraySumCircular(nums)
#     res = sol.maxSubarraySumCircular(nums)
#     if res != ans:
#         print(f'Test: {nums} ; Fail. Ans: {ans}, Res: {res}')

tests = [
    ([1,-2,3,-2], 3),
    ([5,-3,5], 10),
    ([-3,-2,-3], -2),
    ([-1, 9, -4, 3, 7], 18),
    ([10, 2, -7, 7, -4], 15),
    ([7, 7, -6, -4, 3], 17),
    ([10, -7, 1, -3, 6], 16),
    ([8, 6, -3, 2, -5, 7], 21),
    ([9, 10, -8, 7, -8, 10], 29),
    ([-10,-7,9,-7,6,9,-9,-4,-8,-5], 17),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.maxSubarraySumCircular(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
