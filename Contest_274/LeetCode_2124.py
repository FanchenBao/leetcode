# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def checkString(self, s: str) -> bool:
        if 'a' not in s or 'b' not in s:
            return True
        for i in range(s.find('b'), len(s)):
            if s[i] == 'a':
                return False
        return True



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
