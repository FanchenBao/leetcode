# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        lst = sentence.split(' ')
        for i in range(len(lst) - 1):
            if lst[i][-1] != lst[i + 1][0]:
                return False
        return lst[-1][-1] == lst[0][0]
        

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
