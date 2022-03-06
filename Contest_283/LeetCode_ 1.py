# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        ul, lr = s.split(':')
        col_s, col_e = ul[0], lr[0]
        row_s, row_e = int(ul[1]), int(lr[1])
        res = []
        for c in range(ord(col_s), ord(col_e) + 1):
            res.extend([f'{chr(c)}{r}' for r in range(row_s, row_e + 1)])
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
