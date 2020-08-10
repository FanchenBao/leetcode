# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for p, le in enumerate(s[::-1]):
            res += 26**p * (ord(le) -64)
        return res


sol = Solution()

print(sol.titleToNumber('ZY'))

# for i, test in enumerate(tests):
#     (s, wordDict), ans = test
#     res = sol.wordBreak(s, wordDict)
#     if res == ans:
#         print(f'Test {i + 1}: PASS')
#     else:
#         print(f'Test {i + 1}: Fail. Received: {res}, Expected: {ans}')
