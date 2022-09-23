# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def reverseWords(self, s: str) -> str:
        """LeetCode 557

        72 ms, faster than 45.57% 
        """
        return ' '.join(w[::-1] for w in s.split())

# sol = Solution()
# tests = [
#     ([4,2,1,3], [[1,2],[2,3],[3,4]]),
#     ([1,3,6,10,15], [[1,3]]),
#     ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
# ]

# for i, (arr, ans) in enumerate(tests):
#     res = sol.minimumAbsDifference(arr)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
