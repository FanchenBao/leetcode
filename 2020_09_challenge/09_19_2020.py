# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        """Pretty easy"""
        digits: str = '123456789'
        res = []
        for l in range(len(str(low)), len(str(high)) + 1):
            for i in range(0, 9 - l + 1):
                n = int(digits[i:i + l])
                if low <= n <= high:
                    res.append(n)
                elif n > high:
                    break
        return res


sol = Solution()
tests = [
    (100, 300, [123, 234]),
    (1000, 13000, [1234, 2345, 3456, 4567, 5678, 6789, 12345]),
]

for i, (low, high, ans) in enumerate(tests):
    res = sol.sequentialDigits(low, high)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
