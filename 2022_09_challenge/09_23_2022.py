# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def concatenatedBinary(self, n: int) -> int:
        """LeetCode 1680

        Go front to back. This way, we only need to shift len(bin(v)) - 2 each
        time, which is fewer than 17. Plus, each time we can use MOD to reduce
        the size of res, such that the shift won't create too big a value.

        4959 ms, faster than 10.24%
        """
        res = 0
        MOD = 10**9 + 7
        for v in range(1, n + 1):
            res = ((res << (len(bin(v)) - 2)) + v) % MOD
        return res


class Solution2:
    def concatenatedBinary(self, n: int) -> int:
        """Naive solution.

        4249 ms, faster than 15.75%
        """
        return int(''.join(bin(v)[2:] for v in range(1, n + 1)), 2) % (10**9 + 7)


class Solution3:
    res = [0, 1]
    MOD = 10**9 + 7
    for v in range(2, 100000 + 1):
        res.append(((res[-1] << (len(bin(v)) - 2)) + v) % MOD)
    
    def concatenatedBinary(self, n: int) -> int:
        """Cheap shot

        143 ms, faster than 99.21%
        """
        return self.res[n]


sol = Solution1()
tests = [
    (1, 1),
    (3, 27),
    (12, 505379714),
]

for i, (n, ans) in enumerate(tests):
    res = sol.concatenatedBinary(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
