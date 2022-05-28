# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def numberOfSteps(self, num: int) -> int:
        """LeetCode 1342

        46 ms, faster than 39.62%
        """
        res = 0
        while num:
            if num % 2:
                num -= 1
            else:
                num //= 2
            res += 1
        return res


sol = Solution()
tests = [
    (14, 6),
    (8, 4),
    (123, 12),
]

for i, (num, ans) in enumerate(tests):
    res = sol.numberOfSteps(num)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
