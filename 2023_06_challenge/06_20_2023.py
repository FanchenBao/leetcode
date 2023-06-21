# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        """LeetCode 2090

        Sliding window.

        O(N), 1703 ms, faster than 48.31%
        """
        N = len(nums)
        res = [-1] * N
        lo = s = 0
        for hi in range(N):
            s += nums[hi]
            if hi - lo + 1 == 2 * k + 1:
                res[(lo + hi) // 2] = s // (2 * k + 1)
                s -= nums[lo]
                lo += 1
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
