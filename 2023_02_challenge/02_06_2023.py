# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import chain


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """LeetCode 1470

        63 ms, faster than 70.68% 
        """
        return list(chain(*[[x, y] for x, y in zip(nums, nums[n:])]))
        

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
