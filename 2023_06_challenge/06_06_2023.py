# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        """LeetCode 1502

        O(NlogN) 41 ms, faster than 85.75%
        """
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False
        return True

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
