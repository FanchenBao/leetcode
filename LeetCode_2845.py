# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        cnt_good = 0  # count of num % modulo == k
        cnt_bad = 0  # count of consecutive num % modulo != k
        cnt_subarray_bad = 0  # count of number of subarrays whose numbers % modulo != k
        for i, n in enumerate(nums):
            if n % modulo == k:
                cnt_good += 1
            elif i == 0 or nums[i - 1] % modulo == k:
                cnt_subarray_bad += cnt_bad * (cnt_bad + 1) // 2
                cnt_bad = 1
            else:
                cnt_bad += 1
        res = cnt_subarray_bad if k == 0 else 0
        cur_len = modulo + k
        while cur_len <= cnt_good:
            res += cnt_good - cur_len + 1
            cur_len += modulo
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
