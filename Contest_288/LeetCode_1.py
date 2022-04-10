# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def largestInteger(self, num: int) -> int:
        numstr = str(num)
        evens, odds, res = [], [], []
        for s in numstr:
            n = int(s)
            if n % 2:
                odds.append(n)
                res.append(1)
            else:
                evens.append(n)
                res.append(0)
        evens.sort()
        odds.sort()
        for i, r in enumerate(res):
            if r:
                res[i] = str(odds.pop())
            else:
                res[i] = str(evens.pop())
        return int(''.join(res))


sol = Solution()
tests = [
    (1234, 3412),
    (65875, 87655),
]

for i, (num, ans) in enumerate(tests):
    res = sol.largestInteger(num)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
