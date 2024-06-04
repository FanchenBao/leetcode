# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        """
        Sliding window, rolling sum, and counter to keep track of each potential
        subarray's sum and number of uniques.

        O(N), 437 ms, faster than 21.70%
        """
        res = 0
        cur = 0
        counter = Counter()
        for i, n in enumerate(nums):
            cur += n
            counter[n] += 1
            if i + 1 > k:
                counter[nums[i - k]] -= 1
                if counter[nums[i - k]] == 0:
                    del counter[nums[i - k]]
                cur -= nums[i - k]
            if len(counter) >= m:
                res = max(res, cur)
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
