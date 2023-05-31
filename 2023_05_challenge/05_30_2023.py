# from pudb import set_trace; set_trace()
from typing import List
import math


class MyHashSet:
    """LeetCode 705

    311 ms, faster than 32.41%
    """

    def __init__(self):
        self.hash = [0] * (1000000 + 1)

    def add(self, key: int) -> None:
        self.hash[key] = 1

    def remove(self, key: int) -> None:
        self.hash[key] = 0

    def contains(self, key: int) -> bool:
        return self.hash[key] == 1

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
