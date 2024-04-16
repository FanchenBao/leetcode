# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict, Counter


class Solution1:
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


class Solution2:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        """
        This is a one pass with less space, inspired by lee215's solution in
        the forum.

        The idea is the same, using sliding window. But we use a counter to
        keep track of the frequency of each number. If the current window has
        too many numbers to remove, we shrink it.

        O(N), 1344 ms, faster than 41.50%
        """
        counter: Counter = Counter()
        i = res = 0
        for j, n in enumerate(nums):
            counter[n] += 1
            res = max(res, counter[n])
            if j - i + 1 - res > k:
                counter[nums[i]] -= 1
                i += 1
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
