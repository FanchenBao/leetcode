# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_left, bisect_right


class Solution1:
    def maximumCount(self, nums: List[int]) -> int:
        """O(logN) 133 ms, faster than 43.42%
        """
        i = bisect_left(nums, 0)
        j = bisect_right(nums, 0)
        count_zero = j - i
        return max(i, len(nums) - i - count_zero)


class Solution2:
    def maximumCount(self, nums: List[int]) -> int:
        """O(N), 124 ms, faster than 85.23%
        """
        cnt_neg, cnt_pos = 0, 0
        for n in nums:
            if n > 0:
                cnt_pos += 1
            elif n < 0:
                cnt_neg += 1
        return max(cnt_neg, cnt_pos)

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
