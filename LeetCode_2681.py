# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import accumulate


class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        """Sort nums. Then for each pair of (min, max), we can find the total
        number of groups that can form including min and max. For instance,
        given [v0,v1,v2,v3,v4]

        (v0,v1) => 0C0 = 2^0 = 1 group
        (v0,v2) => 1C0 + 1C1 = 2^1 groups
        (v0,v3) => 2C0 + 2C1 + 2C2 = 2^2 groups
        (v0,v4) => 3C0 + 3C1 + 3C2 + 3C3 = 2^3 groups

        Thus, starting from v0, we have the total score:
        v0 * (2^0 * v1^2 + 2^1 * v2^2 + 2^2 * v3^2 + 2^3 * v4^2)

        Similarly, starting from v1, v2, and v3, we have the total score:
        v1 * (2^0 * v2^2 + 2^1 * v3^2 + 2^2 * v4^2)
        v2 * (2^0 * v3^2 + 2^1 * v4^2)
        v3 * (2^0 * v4^2)

        To compute their sums fast, we can do the following:
        v3 * v4^2
        v2 * (v3^2 + (v4^2) * 2)
        v1 * (v2^2 + (v3^2 + (v4^2) * 2) * 2)
        v0 * (v1^2 + (v2^2 + (v3^2 + (v4^2) * 2) * 2) * 2)

        Finally, do not forget to include all the groups with a single member,
        whose score is the cube of each value.

        O(N), 1077 ms, faster than 33.84%
        """
        MOD = 10**9 + 7
        nums.sort()
        res = sum(pow(n, 3, mod=MOD) for n in nums)  # group of length 1
        pre = 0
        for i in range(len(nums) - 1, 0, -1):
            cur = (2 * pre + pow(nums[i], 2, mod=MOD)) % MOD
            res = (res + cur * nums[i - 1]) % MOD
            pre = cur
        return res


sol = Solution()
tests = [
    ([2,1,4], 141),
    ([1,1,1], 7),
    ([1,1,1,1], 15),
    ([1,2,3,4,5], 1091),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.sumOfPower(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
