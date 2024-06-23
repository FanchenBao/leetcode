# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution1:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        """
        Obtain the indices of all the numbers in nums that MOD modulo equals k
        Then we can count the number of subarrays in this good_indices array
        with a given length using sliding window. We need to include the non-
        good numbers at both ends of the subarray to count extra possible
        subarrays.

        For example, if we have [f, f, t, t, f], and the subarray length is
        two. The total number of good subarrays is (2 + 1) * (1 + 1) = 6

        O(N^2), TLE
        """
        good_indices = [-1]
        for i, n in enumerate(nums):
            if n % modulo == k:
                good_indices.append(i)
        good_indices.append(len(nums))
        cur_len = k
        res = 0
        if cur_len == 0:
            for i in range(1, len(good_indices)):
                cnt = good_indices[i] - good_indices[i - 1] - 1
                res += cnt * (cnt + 1) // 2
            cur_len += modulo
        while cur_len <= len(good_indices):
            for i in range(cur_len, len(good_indices) - 1):
                j = i - cur_len + 1
                res += (good_indices[j] - good_indices[j - 1]) * (
                    good_indices[i + 1] - good_indices[i]
                )
            cur_len += modulo
        return res


class Solution2:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        """
        We will use the same method as problem 1248.

        We turn the numbers in nums that modulo equal to k as 1, otherwise 0.
        Then the problem becomes finding the number of subarrays whose sum also
        modulo equal to k.

        O(N^2) TLE
        """
        counter: Counter = Counter()
        cur_sum = res = 0
        counter[0] = 1
        for n in nums:
            if n % modulo == k:
                cur_sum += 1
            q = 0
            while cur_sum - k - q * modulo >= 0:
                res += counter[cur_sum - k - q * modulo]
                q += 1
            counter[cur_sum] += 1
        return res


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
