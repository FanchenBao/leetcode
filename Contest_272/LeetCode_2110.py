# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        c, res = 1, 0
        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                c += 1
            else:
                res += c * (1 + c) // 2
                c = 1
        return res + c * (1 + c) // 2
        

sol = Solution()
tests = [
    ([3,2,1,4], 7),
    ([8,6,7,7], 4),
    ([1], 1),
]

for i, (prices, ans) in enumerate(tests):
    res = sol.getDescentPeriods(prices)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
