# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right


class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        """
        We find all the pairs that have the same products. Then we check how
        many subsequences we can create within each list of pairs.

        This solution may TLE
        """
        products = defaultdict(list)
        N = len(nums)
        for p in range(N - 4):
            for r in range(p + 4, N):
                products[nums[p] * nums[r]].append([p, r])
        res = 0
        for pairs in products.values():
            for i in range(len(pairs) - 1):
                for j in range(i + 1, len(pairs)):
                    p, r = pairs[i]
                    q, s = pairs[j]
                    if q - p > 1 and r - q > 1 and s - r > 1:
                        res += 1
        return res


class Solution2:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        """
        We will binary search it when we try to create subsequences
        """
        products = defaultdict(list)
        N = len(nums)
        for p in range(N - 4):
            for r in range(p + 4, N):
                products[nums[p] * nums[r]].append([p, r])
        res = 0
        for pairs in products.values():
            for i in range(len(pairs) - 1):
                p, r = pairs[i]
                q_lo = bisect_left(pairs, p + 2, lo=i + 1, key=lambda pair: pair[0])
                q_hi = (
                    bisect_right(pairs, r - 2, lo=i + 1, key=lambda pair: pair[0]) - 1
                )
                for j in range(q_lo, q_hi + 1):
                    if pairs[j][1] - r > 1:
                        res += 1
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
