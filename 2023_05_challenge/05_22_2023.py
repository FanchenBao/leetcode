# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """LeetCode 347

        Use counter. But we implement the counter ourselves here.

        O(NlogN), 121 ms, faster than 29.08%
        """
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        return [n for _, n in sorted([(c, n) for n, c in counter.items()], reverse=True)[:k]]


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
