# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        """Start from either 0 or 1 (doesn't really matter), go through the
        entire derived using XOR to find the original array. Once the last value
        in the original array is found, we can check whether the first value
        of the original array still stands. And that is the answer.

        O(N), 2237 ms, faster than 75.91%
        """
        cur = 0
        for d in derived[:-1]:
            cur ^= d
        return (cur ^ derived[-1]) == 0
        

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
