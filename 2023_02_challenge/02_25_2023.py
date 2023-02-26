# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        """LeetCode 121

        State machine solution.

        O(N), 1123 ms, faster than 48.54% 
        """
        e, h = 0, -math.inf
        for p in prices:
            e, h = max(e, h + p), max(h, 0 - p)
        return e


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        """Use Kadane.

        The problem can be converted to finding the max subarray sum of the diff
        in the original prices. We can do that because prices[j] - prices[j - k]
        = prices[j] - prices[j - 1] + prices[j - 1] - prices[j - 2] + ... +
        prices[j - k + 1] - prices[j - k]

        O(N), 1253 ms, faster than 18.95%
        """
        res, cur_max = 0, 0
        for p in (prices[i + 1] - prices[i] for i in range(len(prices) - 1)):
            cur_max = max(p, p + cur_max)
            res = max(res, cur_max)
        return res


# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
