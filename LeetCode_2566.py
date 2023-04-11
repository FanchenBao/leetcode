# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minMaxDifference(self, num: int) -> int:
        """Find the first non-nine digit, and swap all of its appearances with 9
        This gives us the max.

        Swap all occurrences of the first digit with 0; that gives us the min.

        O(N), 27 ms, faster than 90.90%
        """
        num_str = str(num)
        for le in num_str:
            if le != '9':
                break
        max_num = int(num_str.replace(le, '9'))
        min_num = int(num_str.replace(num_str[0], '0'))
        return max_num - min_num
        

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
