# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """LeetCode 735

        Use stack. O(N), 113 ms, faster than 51.67%
        """
        stack = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                while stack and stack[-1] > 0:
                    pre = stack.pop()
                    if pre + a == 0:
                        break
                    if pre + a > 0:
                        stack.append(pre)
                        break
                else:
                    stack.append(a)
        return stack


class Solution2:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """Combine the first if-else with the while loop.

        O(N), 108 ms, faster than 75.58%
        """
        stack = []
        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                pre = stack.pop()
                if pre + a == 0:
                    break
                if pre + a > 0:
                    stack.append(pre)
                    break
            else:
                stack.append(a)
        return stack

        

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
