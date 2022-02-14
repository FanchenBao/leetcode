# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        res = 0
        while num1 and num2:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            res += 1
        return res

        

# sol = Solution()
# tests = [
#     (9, 6),
#     (2, 2),
#     (9, 6),
#     (20, 6),
#     (21, 6),
#     (22, 8),
#     (23, 8),
#     (100, 54),
# ]

# for i, (n, ans) in enumerate(tests):
#     res = sol.lastRemaining(n)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
