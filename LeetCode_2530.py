# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        """1083 ms, faster than 70.25%
        """
        neg_nums = [-n for n in nums]
        heapq.heapify(neg_nums)
        res = 0
        for _ in range(k):
            v = -heapq.heappop(neg_nums)
            res += v
            heapq.heappush(neg_nums, -math.ceil(v / 3))
        return res


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
