# from pudb import set_trace; set_trace()
from typing import List
from itertools import accumulate
from collections import Counter


class Solution1:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """TLE"""
        psum = list(accumulate(nums))
        res = 0
        for i, ps in enumerate(psum):
            for j in range(i):
                if (ps - psum[j]) % k == 0:
                    res += 1
            if ps % k == 0:
                res += 1
        return res


class Solution2:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """TLE"""
        rc = Counter()
        res = 0
        for n in nums:
            r = n % k
            temp = Counter()
            for key, val in rc.items():
                temp[(key + r) % k] += val
            temp[r] += 1
            res += temp[0]
            rc = temp
        return res


class Solution3:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """LeetCode 974

        This is from lee215

        https://leetcode.com/problems/subarray-sums-divisible-by-k/discuss/217985/JavaC%2B%2BPython-Prefix-Sum

        I was on the right track using remainder, but I neglected an important
        insight: if two numbers mod k have the same remainder, then their
        difference is divisible by k.

        Thus, we can create a prefix-remainder, and for a new prefix-remainder
        we only need to see how many of the previous prefix-remainders that are
        the same as the new one. That is the number of subarrays (including the
        current value) that satisfy the requirement.

        O(N), 328 ms, 44% ranking.
        """
        prefix_remainder = Counter([0])
        pref, res = 0, 0
        for n in nums:
            pref = (pref + n) % k
            res += prefix_remainder[pref]
            prefix_remainder[pref] += 1
        return res


sol = Solution3()
tests = [
    ([4, 5, 0, -2, -3, 1], 5, 7),
    ([5], 9, 0),
    ([0, -5], 10, 1)
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.subarraysDivByK(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
