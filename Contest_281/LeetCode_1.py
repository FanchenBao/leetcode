# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def countEven(self, num: int) -> int:
        c = 0
        for n in range(1, num + 1):
            if sum(int(d) for d in str(n)) % 2 == 0:
                c += 1
        return c
        

        

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
