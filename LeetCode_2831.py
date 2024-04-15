# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        indices = defaultdict(list)
        for i, n in enumerate(nums):
            indices[n].append(i)
        res = 0
        for lst in indices.values():
            i = j = 0
            while j < len(lst):
                if lst[j] - lst[i] - 1 <= k:
                    res = max(res, j - i + 1)
                else:
                    i += 1
                j += 1
            res = max(res, j - i + 1)
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
