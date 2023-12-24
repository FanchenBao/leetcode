# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        """
        Use set to keep track of the positions that are occupied.

        O(N), 640 ms, faster than 99.39%
        """
        occup = set(nums)
        for mf, mt in zip(moveFrom, moveTo):
            occup.remove(mf)
            occup.add(mt)
        return sorted(occup)


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
