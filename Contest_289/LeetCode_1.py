# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            temp = ''
            for i in range(0, len(s), k):
                temp += str(sum(int(d) for d in s[i:i + k]))
            s = temp
        return s


sol = Solution()
tests = [
    ('11111222223', 3, '135'),
    ('00000000', 3, '000'),
]

for i, (s, k, ans) in enumerate(tests):
    res = sol.digitSum(s, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
