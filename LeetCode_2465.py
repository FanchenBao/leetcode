# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        """Use quotient and reminder to represent average.

        O(NlogN), 38 ms, faster than 82.08%
        """
        nums.sort()
        ave = set()
        i, j = 0, len(nums) - 1
        while i < j:
            ave.add(divmod(nums[i] + nums[j], 2))
            i += 1
            j -= 1
        return len(ave)


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
