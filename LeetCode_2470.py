# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution1:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        """I have a problem with this one. I tried to find a sliding window
        solution so that I can solve it in O(N), but while I can compute new
        LCM as the sliding window grows to the right, I cannot figure out a way
        to find new LCM in O(1) time when the left of the window is removed.

        Eventually, this solution is O(N^2). I knew it would work, but got
        hanged on the potential of O(N) solution.

        478 ms, faster than 87.08% 
        """
        lo = hi = -1
        res = 0
        nums.append(k + 1)
        for i, n in enumerate(nums):
            if n <= k and k % n == 0:
                if lo < 0:
                    lo = hi = i
                else:
                    hi = i
            else:
                for j in range(lo, hi + 1):
                    prod = 1
                    for t in range(j, hi + 1):
                        lcm = prod * nums[t] // math.gcd(prod, nums[t])
                        if lcm == k:
                            res += hi - t + 1
                            break
                        prod *= nums[t]
                lo = hi = -1
        return res


class Solution2:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        """Python has lcm function.

        Inspired by https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/discuss/2808843/O(n-d(k)-log(k))
        """
        res = 0
        N = len(nums)
        for i in range(N):
            lcm = 1
            for j in range(i, N):
                if nums[j] > k or k % nums[j]:
                    break
                lcm = math.lcm(lcm, nums[j])
                res += int(lcm == k)
        return res


sol = Solution2()
tests = [
    ([3,6,2,7,1], 6, 4),
    ([3], 2, 0),
    ([5], 5, 1),
    ([69, 95, 20, 36, 71, 18, 94, 81, 50, 57], 18, 1),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.subarrayLCM(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
